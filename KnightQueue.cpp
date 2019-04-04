#include <iostream>
#include <map>
#include <queue>
#include <fstream>
#include <climits>
using namespace std;

int row[] = { 2, 2, -2, -2, 1, 1, -1, -1 };
int col[] = { -1, 1, 1, -1, 2, -2, 2, -2 };

struct Node
{
    int x, y, dist;
    bool operator<(const Node& o) const
    {
        return x < o.x || (x == o.x && y < o.y);
    }
    Node(int x, int y, int dist = 0): x(x), y(y), dist(dist) {}
};

int BFS(Node src, Node dest, int N)
{
    map<Node, bool> visited;
    
    queue<Node> q;
    q.push(src);

    while (!q.empty())
    {
        Node node = q.front();
        q.pop();

        int x = node.x;
        int y = node.y;
        int dist = node.dist;
        
        if (x == dest.x && y == dest.y)
            return dist;

        if (!visited.count(node))
        {
            visited[node] = true;

            for (int i = 0; i < 8; ++i) 
            {
                int x1 = x + row[i];
                int y1 = y + col[i];

                if (!(x1 < 0 || y1 < 0 || x1 >= N || y1 >= N))
                    q.push({x1, y1, dist + 1});
            }
        }
    }
    return -1;
}

int main(int argc, char **argv)
{   
    if(argc==3){
      string inputfile = argv[1];
      string outputfile = argv[2];
      int N,Sx,Sy,Dx,Dy,result;
      ifstream infile;
      infile.open(inputfile);
      infile >> N;
      infile >> Sx;
      infile >> Sy;
      infile >> Dx;
      infile >> Dy;
      Node src = {Sx, Sy};

      Node dest = {Dx, Dy};

      result = BFS(src, dest, N);

      ofstream outfile;
      outfile.open(outputfile);
      outfile << result << endl;
    }else{
      cout<<"Please provide 3 arguments"<<endl;
    }
    
    return 0;
}
