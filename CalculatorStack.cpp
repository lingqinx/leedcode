#include<iostream>
#include<fstream>
#include<stack>
#include<deque>
#include <iomanip>
#include<string>
using namespace std;

int Priority(char c) 
{
  switch(c) 
  {
  case '+':
  case '-':
    return 0; 
    break;
  case '*':
  case '/':
    return 1; 
    break;
  case '(':
  case ')':
    return -1; 
    break;
   }
}

void check(char c, stack<char>& operation, deque<char>& postfix_expression) 
{  
  if(operation.empty()) 
  {
    operation.push(c);
    return;
  }
 
  if(c=='('||c==')') 
  {
    if(c=='(') 
      operation.push(c);
    else {
      while(operation.top()!='(') 
      {  
        char ch = operation.top();
        postfix_expression.push_back(ch);
        operation.pop();
      }
 
      operation.pop();  
    }
  }else {
    char sym = operation.top();  
 
    if(Priority(c)<=Priority(sym))  
    {
      operation.pop();
      postfix_expression.push_back(sym);
      check(c,operation,postfix_expression); 
    }else 
    {
      operation.push(c);  
    }
  }
}
 
void calculate(deque<char>& postfix_expression, stack<float>& calcu) 
{  
  while(!postfix_expression.empty()) 
  {
    char c = postfix_expression.front();
    postfix_expression.pop_front();
    
    if(c>='0'&&c<='9') 
    {
      float op = c-'0';    
      calcu.push(op);     
    }else 
    { 
      float op1 = calcu.top();
      calcu.pop();
      float op2 = calcu.top();
      calcu.pop();
      switch(c) 
      {
      case '+':
        calcu.push(op2+op1);
        break;
      case '-':
        calcu.push(op2-op1);
        break;
      case '*':
        calcu.push(op2*op1);
        break;
      case '/':
        calcu.push(op2/op1); 
        break;
      }
    }
  }
}
 
int main(int argc, char **argv)
{
  deque<char> infix_expression,postfix_expression; 
  stack<char> operation; 
  stack<float> calcu;
  string str;
  if(argc==3){
    string inputfile = argv[1];
    string outputfile = argv[2];
    ifstream infile;
    infile.open(inputfile);
    infile>>str;
    for(int i=0;i!=str.size();++i) 
    {
      infix_expression.push_back(str[i]);  
    }
   
    while(!infix_expression.empty()) 
    {
      char c = infix_expression.front();
      infix_expression.pop_front();
   
      if(c>='0'&&c<='9')
      {
        postfix_expression.push_back(c);
      }else {
        check(c,operation,postfix_expression);  
      }
   
    }
    while(!operation.empty()) 
    {  
      char c = operation.top();
      postfix_expression.push_back(c);
      operation.pop();
    } 
    calculate(postfix_expression,calcu);  
    float result = calcu.top();
    ofstream outfile;
    outfile.open(outputfile);
    outfile<<setiosflags(ios::fixed)<<setprecision(2)<<result<<endl;
  }else{
    cout<<"Please provide 3 arguments"<<endl;
  }
  
}