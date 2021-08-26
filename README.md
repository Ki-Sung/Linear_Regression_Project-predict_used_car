# Linear Regression Project - Predict used car price

<img src="https://user-images.githubusercontent.com/80456601/119268747-4b6f4400-bc2f-11eb-835e-65dcbf6a2a59.png" width="60%" height="60%"/>

- 프로젝트 목적: kaggle에서 주최한 "**인도 중고차 예측하기**" 데이터를 바탕으로 인도 중고차 가격과 거래하기 좋은 지역 예측하기
- 데이터: kaggle의 [인도 중고차 예측하기](https://www.kaggle.com/avikasliwal/used-cars-price-prediction) 데이터셋
- 프로젝트 기간: 2021.04.20 ~ 2021.05.20
- 최종 발표일: 2021.05.20
- 발표자: 김영진 (팀장)
- 팀원: 
  - [김영진 (팀장)](https://github.com/Andy-yeongjin): EDA, 모델링 구축(Linear Regression, Random Forest), 모델링 검증
  - [박창현](https://github.com/qkrckdgus1015): EDA, 시장 분석을 위한 중고차에 관한 논문 참고
  - [김기성](https://github.com/Ki-Sung): 데이터 파악 후 EDA, 비쥬얼라이제이션 담당, 모델링에 필요한 Feature 파악
- 첨삭: 
  - [민형기 강사님](https://github.com/PinkWink)
  - [정현석 클래스 매니저님](https://github.com/FLY-CODE77)
- 사용한 언어
  - [![Python Badge](http://img.shields.io/badge/-Python%20-blue?style=flat-square&&logoColor=yellow&logo=python&link=https://www.python.org/)](https://www.python.org/) [![Numpy Badge](http://img.shields.io/badge/-Numpy%20-013243?style=flat-square&&logoColor=white&logo=numpy&link=https://numpy.org/)](https://numpy.org/) [![Pandas Badge](http://img.shields.io/badge/-Pandas%20-150458?style=flat-square&logoColor=white&logo=pandas&link=https://pandas.pydata.org/)](https://pandas.pydata.org/) [![Matplotlib Badge](http://img.shields.io/badge/-Matplotlib%20-2350A9?style=flat-square&logoColor=white&logo=matplotlib&link=https://matplotlib.org/)](https://matplotlib.org/) [![Seaborn Badge](http://img.shields.io/badge/-Seaborn%20-212E50?style=flat-square&logoColor=white&logo=seaborn&link=https://seaborn.pydata.org/)](https://seaborn.pydata.org/) [![Pyecharts Badge](http://img.shields.io/badge/-Pyecharts%20-34E0A1?style=flat-square&logoColor=black&logo=pyecharts&link=https://pyecharts.org/)](https://pyecharts.org/) [![Sklearn Badge](http://img.shields.io/badge/-Sklearn%20-F7931E?style=flat-square&logoColor=black&logo=scikit-learn&link=https://scikit-learn.org/stable/)](https://scikit-learn.org/stable/)

## 프로젝트 과정

<img src="https://user-images.githubusercontent.com/80456601/131045057-95de77e8-daa8-406d-a5f5-0f27627b95c2.png" width="80%" height="80%"/>

1. DB구조 파악 및 Column별 검토
2. 분석에 필요한 Column 추가 및 데이터 전처리 
3. EDA - 데이터 탐색 및 모델링에 필요한 Feature 파악
4. 모델 분석 및 구축
- LinearRegression 모델 구축
- RandomForest 모델 구축
5. 모델 검증
- LinearRegression 모델 검증
  1) 설명 분산 점수: 0.78, 평균 제곱 오차: 27.08, 결정 계수: 0.78
  2) 로그를 씌운 점수 - 설명 분산 점수: 0.92, 평균 제곱 오차: 0.01, 결정 계수: 0.92
- RandomForest 모델 검증
  1) 설명 분산 점수: 0.91, 평균 제곱 오차: 10.53, 결정 계수: 0.92
  2) 로그를 씌운 점수 - 설명 분산 점수: 0.94, 평균 제곱 오차: 0.008, 결정 계수: 0.94
6. 최종 결과
- 중고차 가격 예측값 
  - 마루티 스즈키 Swift VVT VXL 모델 (실제 중고차 가격 4.85 라크) 
    - LinearRegression log 모델: 5.08 라크로 예측 (0.23 라크 차이)
    - RandomForest log 모델:6.23 라크로 예측 (1.38 라크 차이)
  - 현대 Grand i10 1.2 CRDi Sport option 모델 (실제 중고차 가격 5.55 라크)
    - LinearRegression log 모델: 6.01 라크로 예측 (-0.46 라크 차이)
    - RandomForest log 모델:4.63 라크로 예측 (0.92 라크 차이)
- 중고차 가격을 잘 받을 수 있는 인도 지역 예측
  - 마루티 스즈키 거래시 Kolkata 지역 
  - 현대 거래시 Kolkata 지역 
  - 혼다 거래시 Kolkata 지역
  - 토요타 거래시 Mumbai 지역 
  - 벤츠 거래시 Munbai 지역

## 프로젝트 결과
<img src="https://user-images.githubusercontent.com/80456601/120070388-40039900-c0c5-11eb-8611-8aaaf61746b6.png" width="80%" height="80%"/>

- 사용한 모델 중 반복적인 모델링을 돌려 본 결과 'LinearRegression'과'RandomForestRegressor' 정확도가 높아 두 모델을 체택
- 'LinearRegression'는 설명 분산 점수: 0.78, 평균 제곱 오차: 27.08, 결정 계수: 0.78 / 'RandomForestRegressor'는 0.91, 평균 제곱 오차: 10.53, 결정 계수: 0.92으로 'RandomForestRegressor'의 정확도가 높음.
- 모델의 정확도를 올리기 위해(결정 계수의 차이를 줄이기 위해) log를 씌워본 결과 'LinearRegression'는 결정 계수: 0.78 -> 0.92, 평균 제곱 오차: 27.08 -> 0.01 / 'RandomForestRegressor'는 결정 계수: 0.92 -> 0.94, 평균 제곱 오차: 10.53 -> 0.008로 정확도가 상승. 
- 마루티 스즈키 Swift VVT VXL 모델을 기준 실제 중고차 가격과 예측값을 비교해본 결과 LinearRegression log 모델 사용시 0.23 라크 차이, RandomForest log 모델 사용시 1.38 라크 차이 / 현대 Grand i10 1.2 CRDi Sport option 모델 기준 실제 중고차 가격과 예측값을 비교해본 결과 LinearRegression log 모델 사용시 -0.46 라크 차이, RandomForest log 모델 사용시 0.92 라크 차이라는 결과 도출
<img src="https://user-images.githubusercontent.com/80456601/131046631-1de38bab-ecd1-4696-9c3f-6142be270dbb.png" width="80%" height="80%"/>

- 인도시장에서 중고차 거래시 가격을 잘 받을 수 있는 인도 지역을 예측해본 결과 마루티 스즈키 거래시 Kolkata 지역 / 현대 거래시 Kolkata 지역 / 혼다 거래시 Kolkata 지역 / 토요타 거래시 Mumbai 지역 / 벤츠 거래시 Munbai 지역으로 결과가 도출됨

### [자세한 코드와 프로젝트 과정을 보시려면 여기를 클릭](https://nbviewer.jupyter.org/github/Ki-Sung/Linear_Regression_Project-predict_used_car/blob/main/used_car_final.ipynb)
