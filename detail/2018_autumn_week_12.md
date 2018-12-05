# Add create table
This is used for quick search for managers.

```sql
create table volunteer(
student_mobilephone char(11),
student_university enum('thu', 'pku', 'hit', 'sust', 'szu', 'siat', 'szpt'),
student_gender enum('Male','Female'),
student_birthdate date,
student_birthplace varchar(16),
student_major varchar(10),
student_email varchar(25),
student_wechat_id varchar(25),
student_qq varchar(10),
student_type enum('Doctor', 'Undergraduate', 'Master'),
student_enter_university_time char(4),
student_clothing_size enum('M', 'S', 'L', 'XL', '2XL', '3XL'),
primary key(student_mobilephone)
)
```