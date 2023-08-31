# Consultas a la base de datos eoi2
**1. Nombre y edad de los empleados.**\
SELECT nombre, edad FROM empleados;

__2. Salario y trienios de cada categoría si suponemos un aumento del 2%.__\
SELECT salario * 1.02 as salario_aumentado, trienio * 1.02 as trienio_aumentado FROM categorias;

**3. Año de contratación de cada empleado.**\
SELECT nombre, contrato, YEAR(contrato) FROM empleados;

__4. Edades de los empleados.__\
SELECT num, edad FROM empleados;

**5. Categorías profesionales que superan las 35.000 de salario.**\
SELECT * FROM categorias WHERE salario > 35000;

__6. Datos del empleado número 1014.__\
SELECT * FROM empleados WHERE num = 1014;

**7. Empleados del departamento 106.**\
SELECT * FROM empleados WHERE departamento = 106;

__8. Empleados cuya contratación se produjo en el año 2000.__\
SELECT * FROM empleados WHERE YEAR(contrato) = 2000;

**9. Empleados que no sean comerciales (código de categoría 4).**\
SELECT * FROM empleados WHERE NOT categoria = 4;

__10. Empleados contratados entre los años 1990 y 1994.__\
SELECT * FROM empleados WHERE YEAR(contrato) BETWEEN 1990 AND 1994;

**11. Categorías que tienen un salario inferior a 35.000 o superior a 40.000.**\
SELECT * FROM categorias WHERE salario NOT BETWEEN 35000 AND 40000;

__12. Empleados cuya categoría es director o jefe de sección (códigos 1 y 2).__\
SELECT * FROM empleados WHERE categoria IN (1, 2);

**13. Empleados de nombre 'Jose'.**\
SELECT * FROM empleados WHERE nombre LIKE '%Jose%';

__14. Empleados que pertenecen a la categoría de administrativo (código 3) y que tienen una edad mayor de 35 años.__\
SELECT * FROM empleados WHERE categoria = 3 AND edad > 35;

**15. Empleados que no pertenecen al departamento 110.**\
SELECT * FROM empleados WHERE departamento<>110;

__16. Nombre y edad de los empleados ordenados por edad.__\
SELECT nombre, edad FROM empleados ORDER BY edad;

**17. Nombre y edad de los empleados ordenados por nombre de forma descendente.**\
SELECT nombre, edad FROM empleados ORDER BY nombre DESC;

__18. Nombre del empleado y de la categoría en el que trabaja.__\
SELECT e.nombre, c.titulo FROM empleados e, categorias c WHERE e.categoria=c.categoria;\
SELECT e.nombre, c.titulo FROM empleados e INNER JOIN categorias c ON e.categoria=c.categoria;

**19. Código y teléfonos de los departamentos de las oficinas de la región 'Centro'.**\
SELECT d.codigo, d.telefono FROM dptoficinas d, oficinas o WHERE d.oficina=o.oficina AND o.region='Centro';

__20. Nombre del empleado y ciudad en la que trabaja.__\
SELECT nombre, ciudad FROM empleados, dptoficinas, oficinas WHERE empleados.departamento=dptoficinas.codigo AND dptoficinas.oficina=oficinas.oficina;

**21. Sueldo de cada empleado incluyendo trienios.**\
SELECT e.num, c.salario + c.trienio * floor(datediff(CURRENT_DATE(), e.contrato)/(365 * 3)) AS sueldo FROM empleados e, categorias c WHERE e.categoria = c.categoria;

__22. Nombre de los empleados y de sus jefes de sección.__\
SELECT empl.nombre AS nombre_empleado, jefe.nombre AS jefe_seccion FROM empleados empl, empleados jefe WHERE empl.departamento=jefe.departamento AND jefe.categoria=2 AND empl.categoria<>1 AND empl.nombre<>jefe.nombre;

**23. Suma del sueldo de los empleados, sin contar trienios.**\
SELECT SUM(salario) AS suma_sueldos FROM empleados, categorias WHERE empleados.categoria=categorias.categoria;

__24. Promedio del sueldo, sin contar trienios, de la oficina de 'Barcelona'.__\
SELECT AVG(salario) AS avg_sueldo_barcelona FROM empleados, categorias, dptoficinas, oficinas WHERE empleados.departamento=dptoficinas.codigo AND dptoficinas.oficina=oficinas.oficina AND empleados.categoria=categorias.categoria AND oficinas.ciudad = 'Barcelona';

**25. Salarios máximo y mínimo de los empleados, incluyendo trienios.**\
SELECT MIN(salario + trienio * floor(datediff(CURRENT_DATE(), contrato)/(365 * 3))) AS min_sueldo, MAX(salario + trienio * floor(datediff(CURRENT_DATE(), contrato)/(365 * 3))) AS max_sueldo FROM empleados, categorias WHERE empleados.categoria = categorias.categoria;

__26. Número de empleados que superan los 40 años.__\
SELECT COUNT(*) AS num_mayores_40 FROM empleados WHERE edad > 40;

**27. Número de edades diferentes que tienen los empleados.**\
SELECT COUNT(DISTINCT edad) AS num_diff_edad FROM empleados;

__28. Categoría y suma de los sueldos de los empleados, contando trienios, de cada una de las categorías.__\
SELECT empleados.categoria, SUM(salario + trienio * floor(datediff(CURRENT_DATE(), contrato)/(365 * 3))) AS suma_sueldos FROM empleados, categorias WHERE empleados.categoria = categorias.categoria GROUP BY empleados.categoria;

**29. Nombre y suma de los sueldos de los empleados, contando trienios, de cada oficina.**\
SELECT oficinas.ciudad, SUM(salario + trienio * floor(datediff(CURRENT_DATE(), contrato)/(365 * 3))) AS suma_sueldos FROM empleados, dptoficinas, oficinas, categorias WHERE empleados.departamento = dptoficinas.codigo AND dptoficinas.oficina=oficinas.oficina AND empleados.categoria=categorias.categoria GROUP BY oficinas.ciudad;

__30. Titulo y suma de trienios de las categorías cuya suma supera las 10000__\
SELECT categorias.titulo, SUM(trienio * floor(datediff(CURRENT_DATE(), contrato)/(365 * 3))) AS suma_sueldos FROM empleados, categorias WHERE empleados.categoria=categorias.categoria GROUP BY categorias.titulo HAVING suma_sueldos>10000;

**31. Nombre del departamento y número de empleados de los departamentos que tienen más de 5 empleados.**\
SELECT departamentos.nombre, COUNT(*) AS num_empleados FROM empleados, dptoficinas, departamentos WHERE empleados.departamento=dptoficinas.codigo AND dptoficinas.departamento=departamentos.deptno GROUP BY departamentos.nombre HAVING num_empleados>5;

__32. Nombre y sueldo, contando trienios, de los empleados cuyos sueldos son inferiores a la media de sueldos de la empresa.__\
SELECT nombre, salario + trienio * floor(datediff(CURRENT_DATE(), contrato)/(365 * 3)) AS sueldo FROM empleados, categorias WHERE empleados.categoria = categorias.categoria AND salario + trienio * floor(datediff(CURRENT_DATE(), contrato)/(365 * 3))<(SELECT AVG(salario+trienio*floor(datediff(CURRENT_DATE(), contrato)/(365 * 3))) FROM empleados, categorias WHERE empleados.categoria = categorias.categoria);

**33. Título de las categorías donde existe un empleado con contrato anterior a 1990.**\
SELECT categorias.titulo FROM empleados, categorias WHERE empleados.categoria=categorias.categoria AND YEAR(empleados.contrato)<1990 GROUP BY categorias.titulo;

SELECT titulo FROM categorias WHERE EXISTS (SELECT * FROM empleados WHERE empleados.categoria=categorias.categoria AND YEAR(contrato)<1990);

__34. Nombre de los empleados que tiene un contrato más antiguo que cualquier empleado del departamento de 'Informática'.__\
SELECT nombre FROM empleados WHERE contrato<(SELECT MIN(empleados.contrato) FROM empleados, dptoficinas, departamentos WHERE empleados.departamento=dptoficinas.codigo AND dptoficinas.departamento=departamentos.deptno AND departamentos.nombre='Informática');

**35. Ciudad y número de empleados de la oficina que tiene un número de empleados superior a la media de la empresa.**\
SELECT oficinas.ciudad, COUNT( * ) AS num_empleados FROM oficinas, empleados, dptoficinas WHERE empleados.departamento=dptoficinas.codigo AND dptoficinas.oficina=oficinas.oficina GROUP BY oficinas.ciudad HAVING num_empleados>(SELECT AVG(num_empleados2) FROM (SELECT COUNT( * ) AS num_empleados2 FROM oficinas, empleados, dptoficinas WHERE empleados.departamento=dptoficinas.codigo AND dptoficinas.oficina=oficinas.oficina GROUP BY oficinas.ciudad) columna);

SELECT oficinas.ciudad, COUNT( * ) AS num_empleados FROM oficinas, empleados, dptoficinas WHERE empleados.departamento=dptoficinas.codigo AND dptoficinas.oficina=oficinas.oficina GROUP BY oficinas.ciudad HAVING num_empleados>((SELECT COUNT( * ) FROM empleados)/(SELECT COUNT( * ) FROM oficinas));