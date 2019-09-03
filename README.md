# Face-Clustering


`Face Clustering`은 비지도 학습(**Unsupervised Learning**) 기반의 얼굴 분류 알고리즘이다. 
즉, 기존 지도학습과는 다르게 label된 데이터셋이 필요없다. 

본 코드에서는 Face Clustering 방법을 통해 label 되지 않은 face images 79개를 분류해보았다.

기본 원리는 다음과 같다. 

#### 1. 이미지에서 얼굴 추출
#### 2. 각각의 얼굴 이미지에서 사람의 눈, 코, 입, 턱의 위치와 윤곽을 잡아내고, 그것을 벡터로 인코딩
#### 3. DBSCAN을 이용하여 인코딩한 결과를 clustering.


**Reference**

https://www.pyimagesearch.com/2018/07/09/face-clustering-with-python/

`Face Clustering` 구현 코드와 설명이 자세히 나와있다.


