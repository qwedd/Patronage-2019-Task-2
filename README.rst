Simple example of using Django framework to show results of simple Machine Learning prediction.
=============================================================================
According to instruction this website have 2 views. First is home page, second is page where we can find table that contains data from db.sqlite3, which were converted to db.sqlite3 from csv file.

Code that was used to create db.sqlite3:
`````
df.to_sql('Salary', sqlite3.Connection('db.sqlite3'), if_exists='append', index=False)
`````

Dynamic table contains all data from db.sqlite3, created with loop:
`````
{% for data in all_salary %}
        <tr>
            <th> {{data.workedyears}} </th>
            <th> {{data.salarybrutto}} </th>
        </tr>
           {% endfor %}
`````


=============================================================================
Author: Łukasz Wysocki.