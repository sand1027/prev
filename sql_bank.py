"""
LeetCode SQL Solution Bank
Easy/Medium SQL problems — submitted as MySQL dialect.
"""

SQL_SOLUTIONS = {
    # ─── Easy ─────────────────────────────────────────────────────
    "combine-two-tables": (
        "mysql",
        """SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId"""
    ),

    "second-highest-salary": (
        "mysql",
        """SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee)"""
    ),

    "employees-earning-more-than-their-managers": (
        "mysql",
        """SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary"""
    ),

    "duplicate-emails": (
        "mysql",
        """SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1"""
    ),

    "customers-who-never-order": (
        "mysql",
        """SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders)"""
    ),

    "department-highest-salary": (
        "mysql",
        """SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
)"""
    ),

    "rising-temperature": (
        "mysql",
        """SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature"""
    ),

    "big-countries": (
        "mysql",
        """SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000"""
    ),

    "find-customer-referee": (
        "mysql",
        """SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL"""
    ),

    "article-views-i": (
        "mysql",
        """SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id"""
    ),

    "invalid-tweets": (
        "mysql",
        """SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15"""
    ),

    "calculate-special-bonus": (
        "mysql",
        """SELECT employee_id,
    CASE WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
         ELSE 0 END AS bonus
FROM Employees
ORDER BY employee_id"""
    ),

    "fix-names-in-a-table": (
        "mysql",
        """SELECT user_id,
    CONCAT(UPPER(SUBSTR(name, 1, 1)), LOWER(SUBSTR(name, 2))) AS name
FROM Users
ORDER BY user_id"""
    ),

    "patients-with-a-condition": (
        "mysql",
        """SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'"""
    ),

    "delete-duplicate-emails": (
        "mysql",
        """DELETE p1
FROM Person p1
JOIN Person p2 ON p1.email = p2.email AND p1.id > p2.id"""
    ),

    "rearrange-products-table": (
        "mysql",
        """SELECT product_id, 'store1' AS store, store1 AS price FROM Products WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2', store2 FROM Products WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3', store3 FROM Products WHERE store3 IS NOT NULL"""
    ),

    "count-salary-categories": (
        "mysql",
        """SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count FROM Accounts WHERE income < 20000
UNION ALL
SELECT 'Average Salary', COUNT(*) FROM Accounts WHERE income BETWEEN 20000 AND 50000
UNION ALL
SELECT 'High Salary', COUNT(*) FROM Accounts WHERE income > 50000"""
    ),

    "the-number-of-employees-which-report-to-each-employee": (
        "mysql",
        """SELECT m.employee_id, m.name,
    COUNT(e.employee_id) AS reports_count,
    ROUND(AVG(e.age)) AS average_age
FROM Employees m
JOIN Employees e ON e.reports_to = m.employee_id
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id"""
    ),

    "primary-department-for-each-employee": (
        "mysql",
        """SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
UNION
SELECT employee_id, department_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(*) = 1"""
    ),

    "triangle-judgement": (
        "mysql",
        """SELECT x, y, z,
    CASE WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes' ELSE 'No' END AS triangle
FROM Triangle"""
    ),

    "consecutive-numbers": (
        "mysql",
        """SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1 AND l1.num = l2.num
JOIN Logs l3 ON l1.id = l3.id - 2 AND l1.num = l3.num"""
    ),

    "product-price-at-a-given-date": (
        "mysql",
        """SELECT product_id,
    IFNULL(
        (SELECT new_price FROM Products
         WHERE product_id = p.product_id AND change_date <= '2019-08-16'
         ORDER BY change_date DESC LIMIT 1),
        10
    ) AS price
FROM (SELECT DISTINCT product_id FROM Products) p"""
    ),

    "last-person-to-fit-in-the-bus": (
        "mysql",
        """SELECT person_name
FROM (
    SELECT person_name,
           SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
) t
WHERE cumulative_weight <= 1000
ORDER BY cumulative_weight DESC
LIMIT 1"""
    ),

    "count-apples-and-oranges": (
        "mysql",
        """SELECT SUM(b.apple_count + IFNULL(c.apple_count, 0)) AS apple_count,
       SUM(b.orange_count + IFNULL(c.orange_count, 0)) AS orange_count
FROM Boxes b
LEFT JOIN Chests c ON b.chest_id = c.chest_id"""
    ),

    "the-number-of-rich-customers": (
        "mysql",
        """SELECT COUNT(DISTINCT customer_id) AS rich_count
FROM Store
WHERE amount > 500"""
    ),

    "percentage-of-users-attended-a-contest": (
        "mysql",
        """SELECT contest_id,
    ROUND(COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id"""
    ),

    "queries-quality-and-percentage": (
        "mysql",
        """SELECT query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(SUM(rating < 3) * 100 / COUNT(*), 2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name"""
    ),

    "monthly-transactions-i": (
        "mysql",
        """SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM Transactions
GROUP BY month, country"""
    ),

    "immediate-food-delivery-ii": (
        "mysql",
        """SELECT ROUND(
    SUM(order_date = customer_pref_delivery_date) * 100 / COUNT(*), 2
) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
)"""
    ),

    "game-play-analysis-iv": (
        "mysql",
        """SELECT ROUND(
    COUNT(DISTINCT a2.player_id) / COUNT(DISTINCT a1.player_id), 2
) AS fraction
FROM Activity a1
LEFT JOIN Activity a2
    ON a1.player_id = a2.player_id
    AND a2.event_date = DATE_ADD(a1.event_date, INTERVAL 1 DAY)
WHERE (a1.player_id, a1.event_date) IN (
    SELECT player_id, MIN(event_date)
    FROM Activity
    GROUP BY player_id
)"""
    ),

    # ─── Medium ───────────────────────────────────────────────────
    "nth-highest-salary": (
        "mysql",
        """CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET N
  );
END"""
    ),

    "rank-scores": (
        "mysql",
        """SELECT score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores"""
    ),

    "department-top-three-salaries": (
        "mysql",
        """SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId AND e2.salary > e.salary
) < 3"""
    ),

    "trips-and-users": (
        "mysql",
        """SELECT request_at AS Day,
    ROUND(SUM(status != 'completed') / COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips
WHERE client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
  AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
  AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at"""
    ),

    "user-activity-for-the-past-30-days-i": (
        "mysql",
        """SELECT activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY activity_date"""
    ),

    "sales-analysis-iii": (
        "mysql",
        """SELECT s.product_id, p.product_name
FROM Sales s
JOIN Product p ON s.product_id = p.product_id
GROUP BY s.product_id
HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31'"""
    ),

    "reported-posts-ii": (
        "mysql",
        """SELECT ROUND(AVG(daily_percent), 2) AS average_daily_percent
FROM (
    SELECT action_date,
        COUNT(DISTINCT r.post_id) * 100 / COUNT(DISTINCT a.post_id) AS daily_percent
    FROM Actions a
    LEFT JOIN Removals r ON a.post_id = r.post_id AND a.extra = 'spam'
    WHERE a.extra = 'spam'
    GROUP BY action_date
) t"""
    ),

    "market-analysis-i": (
        "mysql",
        """SELECT u.user_id AS buyer_id, u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.buyer_id AND YEAR(o.order_date) = 2019
GROUP BY u.user_id"""
    ),

    "top-travellers": (
        "mysql",
        """SELECT u.name,
    IFNULL(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name"""
    ),

    "string-transforms-into-another-string": (
        "mysql",
        """SELECT ROUND(
    AVG(CASE WHEN p.project_id IS NOT NULL THEN 1 ELSE 0 END) * 100, 2
) AS approval_rate
FROM SurveyLog s
LEFT JOIN Project p ON s.project_id = p.project_id"""
    ),

    "average-selling-price": (
        "mysql",
        """SELECT p.product_id,
    IFNULL(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id"""
    ),

    "capital-gainloss": (
        "mysql",
        """SELECT stock_name,
    SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name"""
    ),

    "restaurant-growth": (
        "mysql",
        """SELECT visited_on,
    SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
    ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
FROM (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
) t
WHERE visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM Customer), INTERVAL 6 DAY)"""
    ),

    "friend-requests-ii-who-has-the-most-friends": (
        "mysql",
        """SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id FROM RequestAccepted
) t
GROUP BY id
ORDER BY num DESC
LIMIT 1"""
    ),

    "investments-in-2016": (
        "mysql",
        """SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon FROM Insurance GROUP BY lat, lon HAVING COUNT(*) = 1
)"""
    ),

    "employees-whose-manager-left-the-company": (
        "mysql",
        """SELECT employee_id
FROM Employees
WHERE salary < 30000
  AND manager_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id"""
    ),

    "exchange-seats": (
        "mysql",
        """SELECT
    CASE
        WHEN id % 2 = 1 AND id < (SELECT COUNT(*) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id"""
    ),

    "movie-rating": (
        "mysql",
        """(SELECT u.name AS results
FROM MovieRating mr
JOIN Users u ON mr.user_id = u.user_id
GROUP BY mr.user_id
ORDER BY COUNT(*) DESC, u.name
LIMIT 1)
UNION ALL
(SELECT m.title
FROM MovieRating mr
JOIN Movies m ON mr.movie_id = m.movie_id
WHERE DATE_FORMAT(mr.created_at, '%Y-%m') = '2020-02'
GROUP BY mr.movie_id
ORDER BY AVG(mr.rating) DESC, m.title
LIMIT 1)"""
    ),

    "students-and-examinations": (
        "mysql",
        """SELECT s.student_id, s.student_name, sub.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name"""
    ),

    "managers-with-at-least-5-direct-reports": (
        "mysql",
        """SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)"""
    ),

    "confirmation-rate": (
        "mysql",
        """SELECT s.user_id,
    ROUND(AVG(c.action = 'confirmed'), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id"""
    ),
}
