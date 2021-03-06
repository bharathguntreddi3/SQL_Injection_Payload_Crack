-- An Example To Demonstrate How SQL_Injection basically Works

CREATE TABLE DEPARTMENT
(
   deptcode int(10) NOT NULL PRIMARY KEY,
   deptname varchar(30),
   location varchar(33)
);

CREATE TABLE EMPLOYEE
(
   EmpCode int(4) PRIMARY KEY,
   EmpFName varchar(15),
   EmpLName varchar(15),
   Job varchar(45),
   Manager varchar(4),
   HireDate date,
   Salary int(6),
   Commission int(6),
   DEPTCODE int(2)
);

INSERT INTO DEPARTMENT VALUES(10, 'FINANCE', 'EDINBURGH'),
INSERT INTO DEPARTMENT VALUES(20,'SOFTWARE','PADDINGTON'),
INSERT INTO DEPARTMENT VALUES(30, 'SALES', 'MAIDSTONE'),
INSERT INTO DEPARTMENT VALUES(40,'MARKETING', 'DARLINGTON'),
INSERT INTO DEPARTMENT VALUES(50,'ADMIN', 'BIRMINGHAM');
                       
INSERT INTO EMPLOYEE  VALUES(9369, 'TONY', 'STARK', 'SOFTWARE ENGINEER', 7902, '1980-12-17', 2800,0,20),
INSERT INTO EMPLOYEE  VALUES(9499, 'TIM', 'ADOLF', 'SALESMAN', 7698, '1981-02-20', 1600, 300,30),    
INSERT INTO EMPLOYEE  VALUES(9566, 'KIM', 'JARVIS', 'MANAGER', 7839, '1981-04-02', 3570,0,20),
INSERT INTO EMPLOYEE  VALUES(9654, 'SAM', 'MILES', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30),
INSERT INTO EMPLOYEE  VALUES(9782, 'KEVIN', 'HILL', 'MANAGER', 7839, '1981-06-09', 2940,0,10),
INSERT INTO EMPLOYEE  VALUES(9788, 'CONNIE', 'SMITH', 'ANALYST', 7566, '1982-12-09', 3000,0,20),
INSERT INTO EMPLOYEE  VALUES(9839, 'ALFRED', 'KINSLEY', 'PRESIDENT', 7566, '1981-11-17', 5000,0, 10),
INSERT INTO EMPLOYEE  VALUES(9844, 'PAUL', 'TIMOTHY', 'SALESMAN', 7698, '1981-09-08', 1500,0,30),
INSERT INTO EMPLOYEE  VALUES(9876, 'JOHN', 'ASGHAR', 'SOFTWARE ENGINEER', 7788, '1983-01-12',3100,0,20),
INSERT INTO EMPLOYEE  VALUES(9900, 'ROSE', 'SUMMERS', 'TECHNICAL LEAD', 7698, '1981-12-03', 2950,0, 20),
INSERT INTO EMPLOYEE  VALUES(9902, 'ANDREW', 'FAULKNER', 'ANAYLYST', 7566, '1981-12-03', 3000,0, 10),
INSERT INTO EMPLOYEE  VALUES(9934, 'KAREN', 'MATTHEWS', 'SOFTWARE ENGINEER', 7782, '1982-01-23', 3300,0,20),
INSERT INTO EMPLOYEE  VALUES(9591, 'WENDY', 'SHAWN', 'SALESMAN', 7698, '1981-02-22', 500,0,30),
INSERT INTO EMPLOYEE  VALUES(9698, 'BELLA', 'SWAN', 'MANAGER', 7839, '1981-05-01', 3420, 0,30),
INSERT INTO EMPLOYEE  VALUES(9777, 'MADII', 'HIMBURY', 'ANALYST', 7839, '1981-05-01', 2000, 200, NULL),
INSERT INTO EMPLOYEE  VALUES(9860, 'ATHENA', 'WILSON', 'ANALYST', 7839, '1992-06-21', 7000, 100, 50),
INSERT INTO EMPLOYEE  VALUES(9861, 'JENNIFER', 'HUETTE', 'ANALYST', 7839, '1996-07-01', 5000, 100, 50);

-- The Attacker can access these kinds of credentials of the uses in the websites using the SQL injection

