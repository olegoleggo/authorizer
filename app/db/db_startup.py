from .connection import connection
from loguru import logger
query = """
CREATE TABLE sessions(
    id UUID PRIMARY KEY,
    session UUID,
    active BOOLEAN
);
CREATE TABLE custom_user (
    id UUID PRIMARY KEY,
    gender VARCHAR(10) CHECK (gender IN ('male', 'female')),
    date_birth TIMESTAMP,
    phone_number VARCHAR(18) UNIQUE,
    avatar VARCHAR,
    name VARCHAR(20),
    surname VARCHAR(20),
    lastname VARCHAR(20),
    qr VARCHAR(255),
    session UUID REFERENCES sessions(id) ON DELETE CASCADE
);
CREATE TABLE university (
    id UUID PRIMARY KEY ,
    name VARCHAR(60),
    city VARCHAR(50),
    address VARCHAR(100),
    website VARCHAR(100),
    email VARCHAR(254)
);
CREATE TABLE study_group(
    id UUID PRIMARY KEY,
    university UUID REFERENCES university(id),
    name VARCHAR(60),
    course SMALLINT,
    type_education VARCHAR CHECK ( type_education in ('магистратура', 'бакалавриат', 'специалитет') )
);
CREATE TABLE teacher(
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES custom_user(id) ON DELETE CASCADE,
    group_id UUID REFERENCES study_group(id) ON DELETE CASCADE,
    department VARCHAR(55)
); 
CREATE TABLE student (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES custom_user(id) ON DELETE CASCADE,
    group_id UUID REFERENCES study_group(id) ON DELETE CASCADE,
    is_headman BOOLEAN DEFAULT false,
    grant_cash VARCHAR(60) DEFAULT false,
    student_ticket_id VARCHAR(20) UNIQUE,
    date_end TIMESTAMP,
    exam_points SMALLINT
);
CREATE TABLE department(
    id UUID PRIMARY KEY,
    university UUID REFERENCES university(id),
    name VARCHAR(60)
);
CREATE TABLE discipline(
    id UUID PRIMARY KEY,
    university UUID REFERENCES university(id),
    name VARCHAR(60)
);
CREATE TABLE study_groups(
    id UUID PRIMARY KEY,
    group_id UUID REFERENCES study_group(id) ON DELETE CASCADE,
    student_id UUID REFERENCES student(id) ON DELETE CASCADE
);
CREATE TABLE discipline_teacher(
    id UUID PRIMARY KEY,
    discipline_id UUID REFERENCES discipline(id) ON DELETE CASCADE, 
    teacher_id UUID REFERENCES teacher(id) ON DELETE CASCADE
);
CREATE TABLE teacher_department(
    id UUID PRIMARY KEY,
    teacher_id UUID REFERENCES teacher(id) ON DELETE CASCADE,
    department_id UUID REFERENCES department(id) ON DELETE CASCADE
);
"""


async def db_startup():
    try:
        connect = await connection()
        await connect.execute(query)
    except Exception as error:
        logger.error(error)



