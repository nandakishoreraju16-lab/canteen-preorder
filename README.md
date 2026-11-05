# Canteen Pre-Order

Students see the canteen menu, order food with their roll number and pick it up when it is ready.
Canteen staff add items, mark items sold out and move each order forward: placed → preparing → ready → collected.

Backend: FastAPI + SQLite · Frontend: React

## Team

| # | Name | Work |
|---|---|---|
| 1 | Monica | Backend |
| 2 | Jyoshana | Backend |
| 3 | Nanda Kishore Raju | Frontend |

## Day 1 plan

| Name | What we will do today |
|---|---|
| Jyoshna | Create `canteen.db` with the `menu_items` and `orders` tables and the sample data. Endpoints E1 to E5 (menu, add item, sold out, place order, one order) and their rules (sold out, 2 orders limit). |
| Monica | Endpoints E6 to E10 (my orders, next status, cancel, kitchen queue, today's sales) and their rules (status order, cancel only when placed). |
| Nanda Kishore Raju | Fill the endpoint table with the backend team. Set up the React app and make the Menu, My orders and Kitchen components. |

## Day 2 plan
| Name | What we will do today |
|---|---|
| Jyoshana | want to solve few logical errors in code and want to write error codes for end points |
| Monica |  |
| Nanda Kishore Raju |  |

## Over all contributions:
## Jyoshna:
I created the database tables, sample data ,developed the first five API endpoints and their backend functions, connected the frontend to the backend, and helped Raju with testing in frotend related to my endpoints.
## Monica:
 I worked on backend tasks E6–E10, which include displaying student orders, updating order status, cancelling orders, managing the kitchen queue, and calculating daily sales. I used Python, FastAPI, SQLAlchemy, and SQLite and tested the APIs using Swagger.

## Nanda Kishore Raju
I created the GitHub repo and the branches, made the README.md file, and updated the Day 1 contributions and work progress in it. Then I started working on the backend. I watched what my teammates were doing and learned new things about the endpoints. I helped fix endpoint errors and solved the merge conflicts. There was a small problem with E4 and E6, so we asked Nithya ma'am and figured it out together. There was one more error in Monica's backend part, about the time, so we asked Rohith sir for a solution and learned something new from it.

After that I started on the frontend: connecting the endpoints, displaying the menu and menu items, checking for errors and fixing them, and asking doubts on WhatsApp at night. I got some new errors in the frontend too, so I asked Rohith sir and fixed them.

The frontend is working now, but from my side I still feel it can be improved.

## API Endpoints

| #   | What it does                                                          | Method | Path                           | Request body / Parameters         | Success code | Error codes   |
| --- | --------------------------------------------------------------------- | ------ | ------------------------------ | --------------------------------- | ------------ | ------------- |
| E1  | Get the menu. Filter by category and show only available items.       | GET    | `/menu`                        | Optional: `category`, `available` | 200          | 422           |
| E2  | Add a new menu item with name, category and price.                    | POST   | `/menu`                        | `name`, `category`, `price`       | 201          | 400, 422      |
| E3  | Mark a menu item available or sold out.                               | PATCH  | `/menu/{item_id}/availability` | `available` (1 or 0)              | 200          | 404, 422      |
| E4  | Place an order using roll number, item ID and quantity.               | POST   | `/orders`                      | `roll_no`, `item_id`, `quantity`  | 201          | 400, 404, 422 |
| E5  | Get an order by its ID, including item name and total price.          | GET    | `/orders/{order_id}`           | `order_id` in path                | 200          | 404           |
| E6  | Get one student's orders for today, newest first.                     | GET    | `/orders/student/{roll_no}`    | `roll_no` in path                 | 200          | 422           |
| E7  | Move an order to its next status.                                     | PATCH  | `/orders/{order_id}/next`      | `order_id` in path                | 200          | 400, 404      |
| E8  | Cancel an order.                                                      | PATCH  | `/orders/{order_id}/cancel`    | `order_id` in path                | 200          | 400, 404      |
| E9  | Get today's kitchen queue with active orders, oldest first.           | GET    | `/kitchen/queue`               | None                              | 200          | —             |
| E10 | Get today's sales, including collected orders and total money earned. | GET    | `/kitchen/sales`               | None                              | 200          | —             |

## Project Progress
1. Created the database tables and added sample data.
2. Developed all 10 backend API endpoints and their functions.
3. started doing frontend.
4. Connected the frontend with the backend.
5. Implemented features like viewing the menu, placing orders, checking order status, cancelling orders, and managing the kitchen queue.
6. Implemented daily sales calculation.
7. Tested the APIs and frontend functionalities.

