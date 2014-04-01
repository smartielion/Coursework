.mode columns
.headers on
.nullvalue NULL
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Course(
    courseNum INT,
    deptID TEXT(4),
    courseName TEXT,
    location TEXT,
    meetDay TEXT CHECK((meetDay NOT LIKE '%S%') OR (meetDay  NOT LIKE '%U%')), /*Saturday denoted as S, Sunday Denoted as U*/
    meetTime datetime CHECK (meetTime BETWEEN "07:00" AND "17:00"),
    
    PRIMARY KEY(courseNum,deptID),
    FOREIGN KEY (deptID) REFERENCES Dept (deptID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
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
    FOREIGN KEY (major) REFERENCES Dept (deptID) 
                                ON UPDATE CASCADE
                                ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Enroll(
    courseNum INT,
    deptID TEXT(4),
    studentID INT,
    PRIMARY KEY(courseNum,deptID,studentID),
    FOREIGN KEY(courseNum,deptID) REFERENCES Course (courseNum,deptID) 
                                    ON UPDATE CASCADE
                                    ON DELETE CASCADE,
    FOREIGN KEY(studentID) REFERENCES Student (studentID) ON UPDATE CASCADE
  
);

--1
SELECT deptID,name
FROM Dept;

--2
SELECT *
FROM Student NATURAL JOIN Enroll NATURAL JOIN Course;

--3
SELECT *
FROM Course
WHERE deptID = 'MATH' and meetDay = 'TR' and meetTime > '12:00';

--4
SELECT courseNum, deptID,courseName, location, meetDay, meetTime
FROM Student NATURAL JOIN Enroll NATURAL JOIN Course
WHERE studentName = 'Alexis';

--5
SELECT *
FROM Student
WHERE (studentID NOT IN(
        SELECT StudentID
        FROM Student NATURAL JOIN Enroll NATURAL JOIN Course
        WHERE (deptID != major)
        )) 
        and (studentID IN(
        SELECT studentID
        FROM Student NATURAL JOIN Enroll NATURAL JOIN Course)
        )
ORDER BY class,major;

--6
SELECT Class, avg(gpa) AS AvgClassGPA
FROM Student
GROUP BY Class;

--7
SELECT *
FROM Student NATURAL JOIN (SELECT avg(gpa) AS AvgGPA, class
FROM Student
GROUP BY class)
WHERE gpa < AvgGPA;

--8
SELECT studentID, studentName, max(count) AS numberOfClasses
FROM Student NATURAL JOIN (SELECT count(courseNum) AS count, studentID
FROM Enroll
GROUP BY studentID);

--9
SELECT deptID, min(numStudents) AS count
FROM (SELECT deptID, count(studentID) AS numStudents
FROM Enroll
GROUP BY deptID)
UNION
SELECT deptID, max(numStudents) AS count
FROM (SELECT dpetID, count(studentID) AS numStudents
From Enroll
GROUP BY deptID)

--10
UPDATE Student SET gpa=(gpa+0.5) WHERE major = 'CS';
UPDATE Student SET gpa=(gpa-0.5) WHERE major != 'CS';

--11
INSERT INTO Dept VALUES ('PS','Philosophy','Platos Cave');
INSERT INTO Course VALUES('102', 'PS' ,'Ethics', 'Platos Cave', 'F','08:00');
insert into Enroll values (102, 'PS', 1282);
insert into Enroll values (102, 'PS', 1381);
insert into Enroll values (102, 'PS', 1709);
insert into Enroll values (102, 'PS', 1316);
insert into Enroll values (102, 'PS', 1501);
insert into Enroll values (102, 'PS', 1661);

--12
DELETE FROM Dept WHERE deptID = 'CS';