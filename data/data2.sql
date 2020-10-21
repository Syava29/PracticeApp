--
-- Файл сгенерирован с помощью SQLiteStudio v3.2.1 в Вт окт 20 16:35:39 2020
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: discip_prepod
CREATE TABLE discip_prepod (id_prepod INT REFERENCES prepod (id_prepod), discip CHAR);
INSERT INTO discip (id_prepod, discip) VALUES (3, 'SQL-сервер');
INSERT INTO discip (id_prepod, discip) VALUES (4, 'Web-программирование');
INSERT INTO discip (id_prepod, discip) VALUES (2, 'Автоматизированные системы управления предприятием');
INSERT INTO discip (id_prepod, discip) VALUES (2, 'Автоматическая обработка текстов');
INSERT INTO discip (id_prepod, discip) VALUES (6, 'Адаптационный курс английского языка');
INSERT INTO discip (id_prepod, discip) VALUES (2, 'Адаптационный курс математики');
INSERT INTO discip (id_prepod, discip) VALUES (6, 'Адаптивные образовательные технологии (Адаптационная специализированная дисциплина)');
INSERT INTO discip (id_prepod, discip) VALUES (7, 'Алгебра');
INSERT INTO discip (id_prepod, discip) VALUES (1, 'Выпуск и сопровождение программных продуктов');
INSERT INTO discip (id_prepod, discip) VALUES (2, 'Вычислительная математика');
INSERT INTO discip (id_prepod, discip) VALUES (3, 'Вычислительные системы, сети и телекоммуникации');
INSERT INTO discip (id_prepod, discip) VALUES (1, 'Имитационное моделирование экономических процессов');
INSERT INTO discip (id_prepod, discip) VALUES (6, 'Иностранный язык');
INSERT INTO discip (id_prepod, discip) VALUES (5, 'Информатика и программирование');
INSERT INTO discip (id_prepod, discip) VALUES (1, 'Информационные системы и технологии');
INSERT INTO discip (id_prepod, discip) VALUES (2, 'Информационные системы финансового учета');
INSERT INTO discip (id_prepod, discip) VALUES (6, 'История');
INSERT INTO discip (id_prepod, discip) VALUES (7, 'Качество и тестирование программного обеспечения');
INSERT INTO discip (id_prepod, discip) VALUES (3, 'Компьютерные сети');
INSERT INTO discip (id_prepod, discip) VALUES (8, 'Маркетинг');
INSERT INTO discip (id_prepod, discip) VALUES (2, 'Машинное зрение');
INSERT INTO discip (id_prepod, discip) VALUES (1, 'Машинное обучение');

-- Таблица: prepod
CREATE TABLE prepod (id_prepod INTEGER PRIMARY KEY AUTOINCREMENT, fio_prepod CHAR);
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (1, 'Строев С.П.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (2, 'Зубкова Л.Н.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (3, 'Чижикова Ю.В.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (4, 'Черкасова В.В.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (5, 'Фролов М.А.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (6, 'Еремеева Н.П.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (7, 'Ломакин Д.Е.');
INSERT INTO prepod (id_prepod, fio_prepod) VALUES (8, 'Русских Т.Н.');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
