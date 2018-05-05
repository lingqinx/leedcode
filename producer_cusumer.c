
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<pthread.h>
#include<unistd.h>
#include<semaphore.h>

#define LINE_SIZE 1024
#define MAX_COUNT 64
#define DELIM " \n\t"
#define MAX 100
extern char **environ;
char *fileName;
char *sortName;
int size;

#define false 0
#define true 1
#define MAX_ACTIVE_THREADS 3 
typedef int bool;
int count;
char buffer[MAX][LINE_SIZE]; 
sem_t full;
sem_t empty;
struct task
{
    void *(*task)(void *arg); 
    void *arg;          
    struct task *next;   
};

typedef struct thread_pool
{
    pthread_mutex_t lock;
    pthread_cond_t cond;
    struct task *task_list;
    
    pthread_t *tids;  
    
    unsigned waiting_tasks; 
    unsigned active_threads; 
    bool shutdown;    
}thread_pool;

typedef struct ARG {
    int id;
    thread_pool *pool;
}ARG;

void quick_sort(int *a,int left,int right){
    int i,j,temp;
    if (left < right)
    {
        i = left;
        j = right;
        temp = a[i];
        while (i < j)
        {
            while (i<j && a[j]>temp)
                j--;
            if (i<j)
                a[i++] = a[j];
            while (i<j && a[i]<temp)
                i++;
            if (i<j)
                a[j--] = a[i];
        }
        a[i] = temp;
        quick_sort(a,left,i-1);
        quick_sort(a,i+1,right);
    }
}

void *CreateFile(void *arg){
    int i;
    int a[size];
    FILE *fp;
    fp = fopen(fileName, "w");
    srand(time(NULL));
    for (i = 0; i < size; i++) {
        a[i] = rand();
        fprintf(fp, "%d ", a[i]);
    }
    fclose(fp);
    pthread_exit(NULL);
}

void *SortNumber(void *arg){
    int i = 0;
    int N = 100;
    int *data;
    data = (int *)malloc(sizeof(int)* N);
    FILE *fp;
    if(( fp=fopen(sortName,"r" ))){
        while(!feof(fp)){
            fscanf(fp, "%d", &data[i++]);
        }
        N = i - 1;
        fclose(fp);
        
        quick_sort(data, 0 , N-1);
        
        fp = fopen(sortName, "w+");
        for(i = 0;i < N;i++){
            fprintf(fp, "data[%d] = %d ", i, data[i]);
        }
        fprintf(fp, "%d ", N);
        fclose(fp);
    }else{
        printf("cannot find the file, please check\n");
    }
    pthread_exit(NULL);
    
}

void deleteHead() {
    for (int i = 1; i < count; i++) {
        strcpy(buffer[i-1], buffer[i]);
    }
    count--;
}

void *Consumer(ARG * arg){
    thread_pool *pool = (thread_pool*)arg->pool;
    struct task *p;
    char command[LINE_SIZE];
    char *fword;
    while(1) {
        sem_wait(&empty);
        pthread_mutex_lock(&pool->lock);
        if (count > 0) {
            strcpy(command, buffer[0]);
            if(!strncmp (command, "quit",4) ){
                exit(0);
            }else if(!strncmp (command, "environ",7)){
                char ** env = environ;
                while (*env)
                    printf("%s\n",*env++);
            }else if(!strncmp (command, "frand",5)){
                fword = strtok(command," ");
                fileName = strtok(NULL," ");
                size = atoi(strtok(NULL," "));

                pthread_t filecreate;
                pthread_create(&filecreate, NULL, CreateFile, NULL);
            }else if(!strncmp (command, "fsort",5)){
                fword = strtok(command," ");
                sortName = strtok(NULL," ");
                pthread_t filesort;
                pthread_create(&filesort, NULL, SortNumber, NULL);
            }else{
                //printf("Worker %d hold the lock, and it will excute the command %s\n",arg->id, command);
                system(command); }
            deleteHead();
        } else {
            //pass
        }
        pthread_mutex_unlock(&pool->lock);
        sem_post(&full);
        sleep(1);
    }
    pthread_exit(NULL);
}

bool pool_init(thread_pool *pool, unsigned int threads_num)
{
    int i;
    pthread_mutex_init(&pool->lock,NULL);
    pthread_cond_init(&pool->cond,NULL);
    
    pool->task_list=malloc(sizeof(struct task));       
    pool->waiting_tasks=0;
    pool->active_threads=threads_num;
    pool->shutdown=false;
    
    pool->tids=malloc(sizeof(pthread_t)*MAX_ACTIVE_THREADS);    
    if(pool->task_list==NULL||pool->tids==NULL)
    {
        perror("allocate memory error");
        return false;
    }
    pool->task_list->next=NULL;
    
    for(i=0;i<pool->active_threads;i++)
    {
        ARG *arg = malloc(sizeof(ARG)*1);
        arg->id = i;
        arg->pool = pool;
        if(pthread_create(&((pool->tids)[i]),NULL,(void*)Consumer,arg)!=0)
        {
            perror("create thread failed!\n");
            return false;
        }
    }
    
    return true;
}

bool destroy_pool(thread_pool *pool)
{
    pool->shutdown = true;
    int i;
    for(i=0;i<pool->active_threads;i++)
    {
        int errno=pthread_join(pool->tids[i],NULL);  
        if(errno!=0)
        {
            printf("join tids[%d] error:%s\n",i,strerror(errno));
        }
        else
            printf("[%u] is joined\n",(unsigned)pool->tids[i]);
    }
    free(pool->task_list);
    free(pool->tids);
    free(pool);
    return true;
}
void *Procucer(char * command){
    thread_pool *pool = malloc(sizeof(thread_pool)*1);
    pool_init(pool, MAX_ACTIVE_THREADS);
    sem_wait(&full);
    pthread_mutex_lock(&pool->lock);
    strcpy(buffer[count++], command);
    pthread_mutex_unlock(&pool->lock);
    sem_wait(&empty);
    pthread_exit(NULL);
}

int main() {
    thread_pool *pool = malloc(sizeof(thread_pool)*1);
    char inputLine[LINE_SIZE];
    char command[LINE_SIZE];
    char *word[MAX_COUNT];
    char **token;
    char *shellPrompt = "myshell->";
    sem_init(&full,0,MAX);
    sem_init(&empty,0,0);
    while(!feof(stdin)){
        system("pwd");
        fputs(shellPrompt, stdout);
        fflush(stdout);
        if(fgets(inputLine, LINE_SIZE, stdin)){
            token = word;
            *token++  = strtok(inputLine, DELIM);
            while((*token++ = strtok(NULL, DELIM)));
            if(word[0]){
                command[0]=0;
                if(!strcmp (word[0], "clr") ){
                    strcpy(command, "clear");
                }else if(!strcmp (word[0], "dir") ){
                    strcpy(command, "ls -al");
                }else if(!strcmp (word[0], "quit") ){
                    strcpy(command, "quit");
                }else if(!strcmp (word[0], "environ") ){
                    strcpy(command, "environ");
                }else if(!strcmp (word[0], "frand") ){
                    int i=1;
                    strcpy(command, "frand");
                    while(word[i]){
                        strcat(command, " ");
                        strcat(command, word[i++]);
                    }
                }else if(!strcmp (word[0], "fsort") ){
                    int i=1;
                    strcpy(command, "fsort");
                    while(word[i]){
                        strcat(command, " ");
                        strcat(command, word[i++]);
                    }
                }else{
                    int i=1;
                    strcpy(command, word[0]);
                    while(word[i]){
                        strcat(command, " ");
                        strcat(command, word[i++]);
                    }
                }
                if(command[0]){
                    pthread_t prod;
                    pthread_create(&prod,NULL,(void *)Procucer,command);
                }
            }
        }
    }
    sem_destroy(&full);
    sem_destroy(&empty);
    destroy_pool(pool);

    return 0;
}
