create table 강의 (
과목명 varchar(100),
과목코드 char(20),
과목코드_분반포함 char(20) NOT NULL,
분반 char(20),
개설대학 char(20),
개설학과 varchar(100),
교수명 varchar(100),
개설학기 char(20),
수강총원 int,
수강인원 int,
비대면여부 char(20),
시간표 varchar(100),
학점 int,
출석비중 int,
중간고사 int,
기말고사 int,
과제 int,
발표 int,
토론 int,
안전교육 int,
기타 int,
etc int,
권장선수과목 varchar(100),
권장후수과목 varchar(100),
primary key(과목코드_분반포함)
);
