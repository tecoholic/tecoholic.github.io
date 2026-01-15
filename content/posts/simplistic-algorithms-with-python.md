---
title: Simplistic Algorithms with Python
date: '2018-03-02T13:23:12'
slug: simplistic-algorithms-with-python
categories:
  - Coding
tags:
  - python
---

I have been working on the problems in Codility to get better at the algorithms and also to expand the way I solve problems in general. One common thing I notice with using Python as the language is that, sometimes the solutions are so simple I wonder if I learnt anything at all.

Take for example, this challenge called [GenomicRangeQuery](https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/) which aims to teach the application of Prefix sums in problem solving. Here is the solution which gets the perfect score of 100% for both accuracy and complexity.

```python
def solution(S, P, Q):
    mins = []

    for i in range(0, len(P)):
        start = P[i]
        end = Q[i]+1
        sub = S[start:end]
        if 'A' in sub:
            mins.append(1)
        elif 'C' in sub:
            mins.append(2)
        elif 'G' in sub:
            mins.append(3)
        else:
            mins.append(4)
    return mins
```

The solution felt like cheating and also, I wasn't sure of the complexity of **in** keyword magic of Python. I searched for a solution in a low level language to understand better. [Here is it in Java](https://rafal.io/posts/codility-genomic-range-query.html). Reproducing for quick comparison.

```java
public static int[] genome(String S, int[] P, int[] Q) {
   int len = S.length();
   int[][] arr = new int[len][4];
   int[] result = new int[P.length];

   for(int i = 0; i < len; i++){
     char c = S.charAt(i);
     if(c == 'A') arr[i][0] = 1;
     if(c == 'C') arr[i][1] = 1;
     if(c == 'G') arr[i][2] = 1;
     if(c == 'T') arr[i][3] = 1;
   }
   // compute prefixes
   for(int i = 1; i < len; i++){
     for(int j = 0; j < 4; j++){
       arr[i][j] += arr[i-1][j];
     }
   }

   for(int i = 0; i < P.length; i++){
     int x = P[i];
     int y = Q[i];

     for(int a = 0; a < 4; a++){
       int sub = 0;
       if(x-1 >= 0) sub = arr[x-1][a];
       if(arr[y][a] - sub > 0){
         result[i] = a+1;
         break;
       }
     }

   }
   return result;
 }
```

Needless to say, the solution is beautiful and as intended (teaches the application of prefix sums).

## Pondering
The difference in the complexity of the two solutions showcases the power and simplicity of Python.

So what am I doing with Python? I am writing simpler code definitely. It is good. I am also worried that I might not be learning a number of techniques that will help in the long run.
