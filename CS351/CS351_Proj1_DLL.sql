.mode columns
.headers on
.nullvalue NULL
PRAGMA foriegn_keys = ON;

CREATE TABLE IF NOT EXISTS Course(
    courseNum INT,
    deptID TEXT,
    courseName TEXT,
    location TEXT,
    meetDay TEXT CHECK((meetDay NOT LIKE '%S%') OR (meetDay  NOT LIKE '%U%')), /*Saturday denoted as S, Sunday Denoted as U*/
    meetTime datetime CHECK (meetTime BETWEEN "07:00" AND "17:00"),
    PRIMARY KEY(courseNum,deptID)
);

CREATE TABLE IF NOT EXISTS Dept(
    deptID TEXT(4) UNIQUE PRIMARY KEY,
    name TEXT,
    building TEXT  
);
    
CREATE TABLE IF NOT EXISTS Student(
    studentID INT PRIMARY KEY,
    studentName TEXT NOT NULL,
    major TEXT,
    class TEXT CHECK((class LIKE 'Sophomore') or (class LIKE 'Freshman') or (class LIKE 'Junior') or (class LIKE 'Senior')),
    gpa REAL CHECK( (gpa ISNULL) OR (gpa >= 0.0) OR (gpa <=4.0) ),
    FOREIGN KEY (major) REFERENCES Dept (deptID) ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Enroll(
    courseNum INT,
    deptID TEXT,
    studentID INT,
    PRIMARY KEY(courseNum,deptID,studentID),
    FOREIGN KEY(courseNum,deptID) REFERENCES Course (courseNum,deptID) ON UPDATE CASCADE,
    FOREIGN KEY(studentID) REFERENCES Student (studentID) ON UPDATE CASCADE
  
);

/*
SELECTION QUERIEs

1.
SELECT deptID,name
FROM Dept
WHERE;

2.
SELECT *
FROM Student NATURAL JOIN Enroll NATURAL JOIN Course
WHERE;

3.
SELECT *
FROM Course
WHERE deptID = 'MATH',meetDay = 'TR',startTime > '12:00';

4.
SELECT courseNum, deptID,courseName, location, meetDay, meetTime
FROM Student NATURAL JOIN Enroll NATURAL JOIN Course
WHERE studentName = 'Alexis';

5.
SELECT studentId, studentName,major,class
FROM Student NATURAL JOIN Enroll NATURAL JOIN Course
WHERE (deptID != major)
ORDER BY (class, major);
*/

/* 
AGGREGATION QUERIES

6.
SELECT deptID,name
FROM Dept
WHERE;

7.
SELECT deptID,name
FROM Dept
WHERE;

8.
SELECT deptID,name
FROM Dept
WHERE;

9.
SELECT deptID,name
FROM Dept
WHERE;

*/