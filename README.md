# 👀 보구보구 BoguBogu
### 청각 장애인을 위한 구화 학습 어플리케이션<br>
"보면서" 학습한다는 의미와 함께 도울 보(輔)와 입 구(口)를 합쳐 **보구보구**라는 이름의 어플리케이션을 제작하였습니다. <br> <br>
<img src="https://user-images.githubusercontent.com/81794559/139928860-365bf511-963f-4c88-9eb0-982c8b057226.png" width="700">

### 청각 장애인이 주로 사용하는 의사 소통 수단이 무엇이라고 생각하시나요?
많은 사람들이 청각 장애인의 메인 의사 소통 수단으로 수화를 생각할텐데 청각 장애인들의 87%는 음성 언어로 대화를 합니다. 하지만 태어나 본인의 말 소리와 주변 사람들의 말 소리를 비교해 가며 자연스럽게 말을 터득하는 청인들과 달리 청각을 활용한 듣기가 불완전한 청각 장애인들의 경우 발화 또한 불안정해 별도의 학습을 필요로 한다고 합니다. 

이 사실을 알고 난 뒤, 저희 숙피치비전은 청각/언어 장애인들의 말하기를 도울 수 있는 소프트웨어를 만들어 보고자 결심했습니다. 

\* 아직은 6개의 단모음과 해당 모음에 'ㄱ', 'ㄴ', 'ㄷ'추가된 글자들만 학습할 수 있다는 것을 참고해 주시길 바랍니다!



## 시스템 구조
<img src="https://user-images.githubusercontent.com/81794559/139930124-f51bdf2c-14da-4733-972d-03dc07aa9a20.png" width="400">

## 실행 화면
### 1. 메인 화면 <br>
<img src="https://user-images.githubusercontent.com/81794559/139940482-1dd4de29-68ab-4404-8843-7e1baabfad52.png" width="400">

### 2. 사용 방법 
<img src="https://user-images.githubusercontent.com/81794559/139936495-9c525fe8-56a5-49c8-88b5-4dcb26c0b119.png" width="400">

### 3. 학습해 보아요, 연습해 보아요의 자음 선택 화면
<img src="https://user-images.githubusercontent.com/81794559/139937860-706b6c7d-7b9b-44f1-888d-e218f8a285de.png" width="400">
<img src="https://user-images.githubusercontent.com/81794559/139938115-1c336532-1413-4dd5-b3b6-3ba744cdc210.png" width="400">

### 4. 학습해 보아요
<img src="https://user-images.githubusercontent.com/81794559/139940123-31f4b6d0-f807-4cdf-9217-d2bec865c215.png" width='400'>

### 5. 연습해 보아요
<img src="https://user-images.githubusercontent.com/81794559/139940850-6fe4c048-c0ec-4528-81ef-fa431f93a040.png" width='400'>

### 6. 판정 화면
#### 맞았을 때
<img src="https://user-images.githubusercontent.com/81794559/139941171-a2ad4479-73ef-43fc-98b9-62069ab71249.png" width='400'>

#### 틀렸을 때
<img src="https://user-images.githubusercontent.com/81794559/139941295-22fbe7a0-2f40-42c6-8739-9df412e6c457.png" width='400'>

### 7. 상세 결과 화면 (음성 스펙트럼)
<img src="https://user-images.githubusercontent.com/81794559/139941461-7cc40fbf-af86-4a9e-8b84-3388644b064a.png" width='400'>

---
### python package version
Django==3.2.5  
dlib @ file:///D:/bld/dlib_1617441823598/work  
imutils==0.5.4  
joblib==1.0.1  
scikit-learn==0.22.2.post1  
opencv==4.0.1  
