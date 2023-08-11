# Final-Project-Tableau

## Project/Goals
1. Data cleaning and data performing
2. Turning data into visual insights, using Tableau
3. Creating impactful dashboards and story to help stakeholder make decisions
4. Communicating insights with the correct visualizations
5. Analyze the happiness score in canada and indentify any trends or intresting insights from that.

## Process
### Step 1:
Data Retrieving and Performing EDA.
### Step 2:
Maps of all countries with their ranks over years.
### Step 3:
Create visualizations and explore the data.
![image](https://github.com/serenasunyu/Midterm_Project/assets/132075292/018e874b-a342-4ad5-8179-aad7724ef3e3)

![image](https://github.com/serenasunyu/Midterm_Project/assets/132075292/f3edd43f-6f2c-4df6-bb64-11b8e35097a2)

### Step 4:
Analysis for Canada Happiness Score Trends
### Step 5:
Building Models

## Results
Results and insights. 
1. Switzerland, Iceland, Denmark, Norway, Finland, Netherlands and Sweden are the best places to live if you goal is to be happy according to the data. All these countries showed up in the top 10 happiest countries in the world for every year from 2015-2022.

2. Canada, while not the happiest place to live in the world according to the happiness index, is still above average when it comes to happiness score. If you don't have an urgent reason to move to another country, you can safely stay here in Canada and not have to worry about being in one of the saddest countries in the world.

3. Canada has a downwards trend of happiness score.

4. The top 10 countries to live in if you want to retire happy.

5. It is interesting to see, based on the linear regression model, the predictors impact the Happiness Score of a Country. Health and freedom contribute more to the Score, and Trust has a lower impact. At the same time, GDP's value is a bit lower than other, we may need to check it in details. p-value shows 0 is not really 0, it far close to zero and then shows as 0. I tested each single year's data, and the p-value in those tests are not 0. 

6. From linear regression predict model, the MSE value of 0.315 is relatively low, indicating that the model's predictions are, on average, close to the actual happiness scores. However, the interpretation of MSE can be subjective based on the scale of your target variable. However, when predict for Canada, the result is differnt from the prediction by using a distribution plot.

7. Linear regression model with Canada's dataset, the result  shows Economy has negtive correlation and Generosity has the most positive correlation with Canada's Happiness Score. Health has also a strong correlation while Family seems has no linear relationship with the Happiness Score. The result on GDP is wried compared with the result on the whole datasets.


## Challenges 
1. A challenge for this project was getting a clear focus on the question to be answered with the data, after some EDA it became more clear.
2. Datasets for Canada is not suffucient
3. GDP vs Score for Canada is wried and can't find the answer for now
4. Limit knowledge about the predict model

## Future Goals
1. If we had more time, we would try and dive more into the history of Canada during these years to see the exact reasons (if any), the happiness score continues to go down, year after year.

2. Make more comparison in terms of before and after covid to see how the indicators' changes afftect the rank or score
