# Face-Clustering


`Face Clustering`은 비지도 학습(**Unsupervised Learning**) 기반이다. 한 마디로 Label 없이 인물 분류를 할 수 있는 방법이다. 단지 Label이 없는 얼굴 데이터만 "적당히" 가지고 있으면 된다. 샘플 코드에서는 129장의 이미지를 학습하여 5명의 얼굴들을 거의 대부분 정확하게 분류해냈다.


본 코드에서는 Face Clustering 를 통해 label 되지 않은 face images들을 자동 분류해보았다.

**Reference**

https://www.pyimagesearch.com/2018/07/09/face-clustering-with-python/

`Face Clustering` 구현 코드와 설명이 자세히 나와있다.


기본적인 원리는 다음과 같다. 

#### 1. 이미지에서 얼굴 추출
#### 2. 각각의 얼굴 이미지에서 사람의 눈, 코, 입, 턱의 위치와 윤곽을 잡아내고, 그것을 벡터로 인코딩
#### 3. DBSCAN을 이용하여 인코딩한 결과를 clustering하는 작업을 거친다.

