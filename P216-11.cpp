// P216-11.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#define N 20

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,t;
	char s[N];
	void px(char a[]);
	
	printf("请输入10个字符：\n");
	puts(s);
   
	px(s);
    
	printf("\n\nafter:\n");
    gets(s);

	return 0;
}
	
	void px(char a[])
	{
		int i,j,t,k;
	    for(k=0;a[k]!='\0';k++);
		for(i=0;i<k-1;i++)
		 for(j=0;j<k-1-i;j++)
			 if(a[j]>a[j+1])
			 {
				 t=a[j];
				 a[j]=a[j+1];
				 a[j+1]=t;
			 }
   }

