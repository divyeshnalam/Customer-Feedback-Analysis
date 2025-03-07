/*Get Average Rating of All Customers*/
SELECT AVG(rating) AS average_rating FROM feedback WHERE rating IS NOT NULL;

/*Get Count of Feedback Per Rating*/
SELECT rating, COUNT(*) AS feedback_count 
FROM feedback 
WHERE rating IS NOT NULL 
GROUP BY rating 
ORDER BY rating DESC;

/*Find Customers Who Gave Low Ratings (≤ 2)*/
SELECT customer_name, feedback_text, rating 
FROM feedback 
WHERE rating <= 2;

/*Find Most Frequent Words in Feedback*/
SELECT feedback_text, COUNT(*) AS occurrences
FROM feedback
GROUP BY feedback_text
ORDER BY occurrences DESC
LIMIT 10;
