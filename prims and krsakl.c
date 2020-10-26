# include <bits/stdc++.h>
using namespace std;

# define V 7
int
parent[V];

int
find(int i)
{
while (parent[i] != i)
    i = parent[i];
return i;
}


void
union1(int
i, int
j)
{
int
a = find(i);
int
b = find(j);
parent[a] = b;
}


void
kruskalMST(int
cost[][V])
{
int
mincost = 0;

for (int i = 0; i < V; i++)
    parent[i] = i;

int
edge_count = 0;
while (edge_count < V - 1) {
int min = INT_MAX, a = -1, b = -1;
for (int i = 0; i < V; i++) {
for (int j = 0; j < V; j++) {
if (find(i) != find(j) & & cost[i][j] < min) {
min = cost[i][j];
a = i;
b = j;
}
}
}

union1(a, b);
printf("Edge %d:(%d, %d) cost:%d \n",
edge_count++, a, b, min);
mincost += min;
}
printf("\n Minimum cost= %d \n", mincost);
}


int
main()
{
int
cost[][V] = {
    {INT_MAX, 28, INT_MAX, INT_MAX, INT_MAX, 10, INT_MAX},
    {28, INT_MAX, 16, INT_MAX, INT_MAX, INT_MAX, 14},
    {INT_MAX, 16, INT_MAX, 12, INT_MAX, INT_MAX, INT_MAX},
    {INT_MAX, INT_MAX, 12, INT_MAX, 22, INT_MAX, 18},
    {INT_MAX, INT_MAX, INT_MAX, 22, INT_MAX, 25, 24},
    {10, INT_MAX, INT_MAX, INT_MAX, 25, INT_MAX, INT_MAX},
    {INT_MAX, 14, INT_MAX, 18, 24, INT_MAX, INT_MAX},
};

kruskalMST(cost);

}

