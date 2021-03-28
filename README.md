# DramaRama web service
Made by Python / Use Django, Pandas
  

## Data preparation
- We surveyed some people and progress the data had been collected.
- we made separate labelling table using table from the top.
- Make it .csv and put the our sqlite3 database.
  
<p align="center">
<img width="60%" src="https://user-images.githubusercontent.com/53461080/101436453-8582ad00-3951-11eb-8008-a64083801453.png" />
<br><br>
drama data
<img width="50%" src="https://user-images.githubusercontent.com/53461080/101436551-ba8eff80-3951-11eb-8be7-9b39278289b5.png" />
</p>
<br>

## Solution
- 입력데이터를 사전데이터와 비교해 드라마를 객체로 가중치 합을 계산하여 최상위 가중치의 드라마 객체를 반환
  - 재이용을 고려해 상위 3개의 드라마 객체 중 랜덤 1개 반환

<p align="center">
<img width="60%" src="https://user-images.githubusercontent.com/53461080/101432006-68e37680-394b-11eb-9fba-b2ab44a142ee.png" />
</p>

```
form_df = form_df.fillna('')  # NaN값 제거
```
### 모든 속성을 비교
```
if col in input_data.keys():  # check there's it
            if type(input_data[col]) == int:
                match = form_df[col] == input_data[col]
                weight_df = form_df[match]
            else:
                for ele in input_data[col]:  # turn all cols in list
                    match = (form_df[col].astype(str)).str.contains(ele)
                    weight_df = pd.concat([weight_df, form_df[match]])

            first = list(weight_df['first'])
            second = list(weight_df['second'])
            third = list(weight_df['third'])
            if not first: continue
            if not second: continue
            if not third: continue
            process_weight(drama_code, first, second, third)  # compute weight
```
### 가중치 계산 함수
```
weight_list = {}  # weight list

def process_weight(drama_code, first, second, third):
    weight = 2  # 가중치
    for step in [first, second, third]:  # type(step) == list
        step = list(filter(lambda e: e != '', step))  # 공백 값 제거
        for elem in step:  # type(elem) == str
            elem = elem.replace(' ', '')  # 글자의 공백제거
            if elem in list(drama_code):
                weight_list[drama_code[drama_code == elem].index[0]] += weight
        weight /= 2
```

# Preview
![image](https://user-images.githubusercontent.com/53461080/110228724-b2d9f980-7f46-11eb-88c9-00a8fcfcf1f8.png)
![image](https://user-images.githubusercontent.com/53461080/110228759-f2a0e100-7f46-11eb-8744-f134a5fbaa84.png)
![image](https://user-images.githubusercontent.com/53461080/110228786-2aa82400-7f47-11eb-9510-8d19c411ddb6.png)
![image](https://user-images.githubusercontent.com/53461080/110228776-08160b00-7f47-11eb-8af8-ca7343fb78da.png)
![image](https://user-images.githubusercontent.com/53461080/110228799-5deab300-7f47-11eb-916e-056a33461ed4.png)
