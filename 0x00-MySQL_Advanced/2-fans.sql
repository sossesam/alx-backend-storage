-- Task 2: 2. Best band ever! - ranks country origins of bands,
-- ordered by the number of (non-unique) fans
SELECT DISTINCT `origin` as `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;