--
-- ���� ������������ � ������� SQLiteStudio v3.2.1 � �� ��� 20 16:35:39 2020
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: discip_prepod
CREATE TABLE discip_prepod (id_prepod INT REFERENCES prepod (id_prepod), discip CHAR);
INSERT INTO discip (id_prepod, discip) VALUES (3, 'SQL-������');
INSERT INTO discip (id_prepod, discip) VALUES (4, 'Web-����������������');
INSERT INTO discip (id_prepod, discip) VALUES (2, '������������������ ������� ���������� ������������');
INSERT INTO discip (id_prepod, discip) VALUES (2, '�������������� ��������� �������');
INSERT INTO discip (id_prepod, discip) VALUES (6, '������������� ���� ����������� �����');
INSERT INTO discip (id_prepod, discip) VALUES (2, '������������� ���� ����������');
INSERT INTO discip (id_prepod, discip) VALUES (6, '���������� ��������������� ���������� (������������� ������������������ ����������)');
INSERT INTO discip (id_prepod, discip) VALUES (7, '�������');
INSERT INTO discip (id_prepod, discip) VALUES (1, '������ � ������������� ����������� ���������');
INSERT INTO discip (id_prepod, discip) VALUES (2, '�������������� ����������');
INSERT INTO discip (id_prepod, discip) VALUES (3, '�������������� �������, ���� � ����������������');
INSERT INTO discip (id_prepod, discip) VALUES (1, '������������ ������������� ������������� ���������');
INSERT INTO discip (id_prepod, discip) VALUES (6, '����������� ����');
INSERT INTO discip (id_prepod, discip) VALUES (5, '����������� � ����������������');
INSERT INTO discip (id_prepod, discip) VALUES (1, '�������������� ������� � ����������');
INSERT INTO discip (id_prepod, discip) VALUES (2, '�������������� ������� ����������� �����');
INSERT INTO discip (id_prepod, discip) VALUES (6, '�������');
INSERT INTO discip (id_prepod, discip) VALUES (7, '�������� � ������������ ������������ �����������');
INSERT INTO discip (id_prepod, discip) VALUES (3, '������������ ����');
INSERT INTO discip (id_prepod, discip) VALUES (8, '���������');
INSERT INTO discip (id_prepod, discip) VALUES (2, '�������� ������');
INSERT INTO discip (id_prepod, discip) VALUES (1, '�������� ��������');

-- �������: prepod
CREATE TABLE prepod (id_prepod INTEGER PRIMARY KEY AUTOINCREMENT, fio_prepod CHAR);
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (1, '������ �.�.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (2, '������� �.�.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (3, '�������� �.�.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (4, '��������� �.�.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (5, '������ �.�.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (6, '�������� �.�.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (7, '������� �.�.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (8, '������� �.�.');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
