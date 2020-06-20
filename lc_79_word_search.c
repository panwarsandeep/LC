#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdint.h>

char tar[10000];
int tarlen;

void printMat(int r, int c, char **mat) {
	int i,j;
	for (i=0; i<r; ++i) {
		for (j=0; j<c; ++j){
			printf("%c ",mat[i][j]);
		}
		printf("\n");
	}
}

typedef struct coord_ {
	int r;
	int c;
}coord;

typedef struct cordstack_ {
	coord *c;
	int cp;
	int len;
} stack;

void push(stack *s, int i, int j) {
	s->c[s->cp].r = i;
	s->c[s->cp].c = j;
	s->cp++;
	//printf("push: %d %d - %d\n",i, j, s->cp-1);
}

bool pop(stack *s, coord *cr) {
	if (s->cp > 0) {
		*cr = s->c[--s->cp];
		//printf("pop: %d %d - %d\n",cr->r, cr->c, s->cp);
		return true;
	} else {
		return false;
	}
}

void printResult(stack *s, char **mat) {
	coord tc;
	if (pop(s, &tc)) {
		printResult(s, mat);
	} else {
		return;
	}
	printf("[%d, %d, %c] ",tc.r, tc.c, mat[tc.r][tc.c]);
}

bool find(int index, char **mat, bool **visited, stack *s, int i, int j, int r, int c) {
	visited[i][j] = 1;
	push(s, i, j);
	//printf("\npushed: %d, %d, ind:%d, %c, tl:%d\n",i,j, index, tar[index], tarlen);
	int ni[] = {1,-1,0,0};
	int nj[] = {0,0,1,-1};
	coord tc;

	if (index == tarlen-1){
		//printf("Matched\n");
		//printResult(s);
		return true;
	} else if (index > tarlen) {
		return false;
	}

	for (int nc=0; nc<4; ++nc) {
		int ti = i + ni[nc];
		int tj = j + nj[nc];
		if ( (ti >=0 && tj >= 0) &&
			 (ti < r && tj < c) &&
			 !visited[ti][tj] && 
			  mat[ti][tj] == tar[index+1]){
				//printf("call: %d, %d\n",ti, tj);
				if (find(index+1, mat, visited, s, ti, tj, r, c)) {
					return true;
				}
		}
	}
	visited[i][j] = 0;
	(void)pop(s, &tc);
	//printf("Popped: %d, %d\n",tc.r, tc.c);
	return false;
}

int main() {
	int r,c;
	int i,j;
	char **mat = (char **)malloc(sizeof(char *)*r);
	bool **visited = (bool **)malloc(sizeof(bool *)*r);

	scanf("%d %d\n",&r, &c);
	for (i=0; i<r; ++i) {
		mat[i] = (char *)malloc(sizeof(char)*c);
		visited[i] = (bool *)calloc(sizeof(bool)*c, 1);
		for (j=0; j<c-1; ++j){
			scanf("%c ", &mat[i][j]);
		}
		scanf("%c\n",&mat[i][j]);
	}
	fgets(tar, 10001, stdin);

	tarlen = strlen(tar);
	tar[tarlen-1] = '\0';
	tarlen -= 1;
	stack s;
	s.c = (coord *)malloc(sizeof(coord)*tarlen);
	s.cp = 0;
	s.len = tarlen;

	//printf("\n%d %d\n",r,c);
	//printMat(r,c, mat);
	//printf("\ntarget: %s, len:%d\n", tar, tarlen);

	for (i=0; i<r; ++i) {
		for (j=0; j<c; ++j){
			if (mat[i][j] == tar[0]) {
				if (find(0, mat, visited, &s, i, j, r, c)) {
					printResult(&s, mat);
					printf("\n");
					return 0;
				}
			}
		}
	}
	printf("-1 -1");
	return 0;

	/* Sample input
	4 4
	A B C D
	E F G H
	I J K L
	M N O P
	ABFJKGH

	sample output:
	[0, 0, A] [0, 1, B] [1, 1, F] [2, 1, J] [2, 2, K] [1, 2, G] [1, 3, H]
	*/
}