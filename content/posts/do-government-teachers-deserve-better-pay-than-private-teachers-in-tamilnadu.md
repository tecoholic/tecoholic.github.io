---
title: Do Government Teachers Deserve Better Pay Than Private Teachers in Tamilnadu?
date: '2019-02-04T00:24:05'
slug: do-government-teachers-deserve-better-pay-than-private-teachers-in-tamilnadu
categories:
  - Social
tags:
  - data
  - society
  - student
---

Recently Tamilnadu's government teachers [went on a strike](https://timesofindia.indiatimes.com/city/chennai/teachers-govt-employees-go-on-indefinite-strike-in-tamil-nadu/articleshow/67639013.cms) and captured the attention of everyone in the state. There were emotions flying from everyone. Around 5 out their 9 demands revolved around money: pay, pension and arrears. An argument which could be heard around was:


> Private school teachers do much more work for much less pay, so government school teachers shouldn't be greedy



Is it really that way? I decided to investigate with whatever little data I could. One key factor that could be used to quantify the workload of teachers is Student-to-Teacher ratio, simply stated, the number of children each teacher is responsible for. Higher the number, more the workload, more notebooks to correct, more exam papers to evaluate, longer queues to handle ... you get the idea.

With that in mind, let us put data to work.

Data Used
---------


* [SSA, Tamil Nadu : Statistics on Student Enrollment by School Management](https://tn.data.gov.in/resources/ssa-tamil-nadu-statistics-student-enrollment-school-management#web_catalog_tabs_block_10)
* [SSA, Tamil Nadu : Statistics on Schools by School Management](https://tn.data.gov.in/resources/ssa-tamil-nadu-statistics-schools-school-management#web_catalog_tabs_block_10)
* [SSA, Tamil Nadu : Statistics on Teachers by School Management](https://tn.data.gov.in/resources/ssa-tamil-nadu-statistics-teachers-school-management#web_catalog_tabs_block_10)


Calculations
------------



With the above sources giving a neat count of schools, students and teachers based on the management type of the school, it was just a matter of selecting the right columns and dividing one by the other.

Student-to-teacher Ratio = No.of Students / No.of Teachers

I uploaded the [dataset to Kaggle](https://www.kaggle.com/tecoholic/tamil-nadu-school-data-ssa) and wrote [a kernel script](https://www.kaggle.com/tecoholic/ratios) to perform the above calculation for each type of schools: Government, Government-Aided, and Private schools.

Observations
------------



Here is the heatmap of the Student to teacher ratios.

![student_teacher_ratios_table](/img/wp-content/uploads/2019/02/student_teacher_ratios_table.png)

There is a clear pattern that can be observed. The government aided school teachers have in some cases twice as much workload as their peers in govt or private schools. Aided school teachers do the work of all the govt. teachers like Census data, Electoral rolls, Election booth staff..etc., too.

Here is graph to give a sense of how far removed are the aided school teachers from their peers.

![student_teacher_ratio_plot](/img/wp-content/uploads/2019/02/student_teacher_ratio_plot.png)
Conclusion
----------



To answer the question asked in the title. I am not sure about government school teachers, but it certainly looks like the govt. aided school teachers deserve better.
