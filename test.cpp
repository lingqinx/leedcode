#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
struct BiTree{
    char data;
    struct BiTree* lchild,*rchild;
};
void CreateBiTree(BiTree* &T, string Input){
    for(int i=0;i<Input.size();i++){
        string s = "";
        if('0'<Input[i]<'9' || 'a'<Input[i]<'z' || 'A'<Input[i]<'Z'){
            
            s = s+ Input[i];}
        
        T = new BiTree;
        T->data = Input[i];
        CreateBiTree(T->lchild);
        CreateBiTree(T->rchild);
        
        
    }
}
void Inorder(BiTree* &T){
    if(T){
        Inorder(T->lchild);
        T->data = T->data - " ";
        string temp = "T->lchild" T->data "T->rchild";
        cout<<temp;
        Inorder(T->lchild);
    }
}
int main(){
    string Input;
    cin>>Input;
    BiTree* T;
    CreateBiTree(T,Input);
    
}

