import unittest
import requests
import logging
import time

logging.basicConfig(level=logging.INFO)

class TestTodoAPI(unittest.TestCase):
    BASE_URL = "http://localhost:4567/todos"

    def setUp(self):
        """Set up the initial state before each test."""
        self.test_todo_id = self.create_test_todo()

    def tearDown(self):
        """Clean up after each test."""
        if self.test_todo_id:
            self.delete_todo(self.test_todo_id)

    def create_test_todo(self):
        """Create a test todo and return its ID."""
        todo_data = {
            "title": "Test Todo",
            "doneStatus": False
        }
        response = requests.post(self.BASE_URL, json=todo_data)
        logging.info(f"Create Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 201)
        return response.json().get("id")

    def delete_todo(self, todo_id):
        """Delete a todo by its ID."""
        response = requests.delete(f"{self.BASE_URL}/{todo_id}")
        logging.info(f"Delete Todo Response: {response.status_code} - {response.text}")
        self.assertIn(response.status_code, [204, 200])

    # /todos
    def test_get_all_todos(self):
        """GET /todos: Test retrieving all todos."""
        response = requests.get(self.BASE_URL)
        logging.info(f"Get All Todos Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json().get('todos'), list)

    def test_create_todo(self):
        """POST /todos: Test creating a todo and measure the time."""
        todo_data = {
            "title": "New Test Todo",
            "doneStatus": False
        }

        start_time = time.time() 
        response = requests.post(self.BASE_URL, json=todo_data)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"Create Todo Response: {response.status_code} - {response.text}")
        logging.info(f"Time taken to create Todo: {elapsed_time:.4f} seconds")

        self.assertEqual(response.status_code, 201)

    def test_delete_todo(self):
        """DELETE /todos/:id: Test deleting a todo and measure the time."""
        todo_data = {
            "title": "Temp Todo for Deletion",
            "doneStatus": False
        }
        create_response = requests.post(self.BASE_URL, json=todo_data)
        self.assertEqual(create_response.status_code, 201, "Failed to create todo for deletion test.")
        
        todo_id = create_response.json().get("id")

        start_time = time.time()
        response = requests.delete(f"{self.BASE_URL}/{todo_id}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"Delete Todo Response: {response.status_code} - {response.text}")
        logging.info(f"Time taken to delete Todo: {elapsed_time:.4f} seconds")

        self.assertIn(response.status_code, [204, 200])

    def test_update_todo(self):
        """PUT /todos/:id: Test updating a todo and measure the time."""
        updated_data = {
            "title": "Updated Todo",
            "doneStatus": True
        }

        start_time = time.time()
        response = requests.put(f"{self.BASE_URL}/{self.test_todo_id}", json=updated_data)
        end_time = time.time()  
        elapsed_time = end_time - start_time
        logging.info(f"Update Todo Response: {response.status_code} - {response.text}")
        logging.info(f"Time taken to update Todo: {elapsed_time:.4f} seconds")

        self.assertEqual(response.status_code, 200)

        response = requests.get(f"{self.BASE_URL}/{self.test_todo_id}")
        logging.info(f"Verify Updated Todo Response: {response.status_code} - {response.text}")
        todo_data = response.json().get('todos', [{}])[0]  
        self.assertEqual(todo_data["title"], "Updated Todo")

    def test_create_multiple_todos(self):
        """Test creating multiple todos and measure the time for each operation."""
        num_todos = 200  
        start_time = time.time()

        for i in range(num_todos):
            todo_data = {
                "title": f"Test Todo {i+1}",
                "doneStatus": False
            }
            response = requests.post(self.BASE_URL, json=todo_data)
            self.assertEqual(response.status_code, 201, f"Failed to create todo {i+1}")
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"Time taken to create {num_todos} todos: {elapsed_time:.4f} seconds")

    def test_update_multiple_todos(self):
        """Test updating multiple todos and measure the time for each operation."""
        num_todos = 200 
        todo_ids = [] 

        # create multiple todos to update
        for i in range(num_todos):
            todo_data = {
                "title": f"Test Todo {i+1}",
                "doneStatus": False
            }
            response = requests.post(self.BASE_URL, json=todo_data)
            self.assertEqual(response.status_code, 201, f"Failed to create todo {i+1}")
            todo_ids.append(response.json().get("id"))

        updated_data = {
            "title": f"Test Todo {i+1}",
            "doneStatus": True 
        }

        start_time = time.time()  

        #update the todos
        for todo_id in todo_ids:
            response = requests.put(f"{self.BASE_URL}/{todo_id}", json=updated_data)
            self.assertEqual(response.status_code, 200, f"Failed to update todo {todo_id}")

        end_time = time.time()  
        elapsed_time = end_time - start_time
        logging.info(f"Time taken to update {num_todos} todos: {elapsed_time:.4f} seconds")

    def test_delete_multiple_todos(self):
        """Test deleting multiple todos and measure the time for each operation."""
        num_todos = 200 
        todo_ids = []

        # Create todos
        for i in range(num_todos):
            todo_data = {
                "title": f"Temp Todo {i+1}",
                "doneStatus": False
            }
            create_response = requests.post(self.BASE_URL, json=todo_data)
            self.assertEqual(create_response.status_code, 201)
            todo_ids.append(create_response.json().get("id"))

        # delete todos
        start_time = time.time()

        for todo_id in todo_ids:
            response = requests.delete(f"{self.BASE_URL}/{todo_id}")
            self.assertIn(response.status_code, [204, 200])

        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"Time taken to delete {num_todos} todos: {elapsed_time:.4f} seconds")

    # /todos/:id/categories
    def test_create_category_for_todo(self):
        """POST /todos/:id/categories: Test creating a category for a todo."""
        category_data = {
            "title": "Test Category"
        }
        response = requests.post(f"{self.BASE_URL}/{self.test_todo_id}/categories", json=category_data)
        logging.info(f"Create Category for Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 201)

    def test_get_categories_for_todo(self):
        """GET /todos/:id/categories: Test retrieving categories for a todo."""
        response = requests.get(f"{self.BASE_URL}/{self.test_todo_id}/categories")
        logging.info(f"Get Categories for Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json().get('categories'), list)

    def test_head_categories_for_todo(self):
        """HEAD /todos/:id/categories: Test headers for categories related to a todo."""
        response = requests.head(f"{self.BASE_URL}/{self.test_todo_id}/categories")
        logging.info(f"Head Categories for Todo Response: {response.status_code}")
        self.assertEqual(response.status_code, 200)

    def test_delete_category_for_todo(self):
        """DELETE /todos/:id/categories/:id: Test deleting a category for a todo."""
        category_data = {"title": "Test Category"}
        post_response = requests.post(f"{self.BASE_URL}/{self.test_todo_id}/categories", json=category_data)
        category_id = post_response.json().get("id")

        response = requests.delete(f"{self.BASE_URL}/{self.test_todo_id}/categories/{category_id}")
        logging.info(f"Delete Category for Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

    # /todos/:id/tasksof
    def test_get_tasks_for_todo(self):
        """GET /todos/:id/tasksof: Test retrieving tasks related to a todo."""
        response = requests.get(f"{self.BASE_URL}/{self.test_todo_id}/tasksof")
        logging.info(f"Get Tasks for Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

    def test_create_task_for_todo(self):
        """POST /todos/:id/tasksof: Test creating a task for a todo."""
        task_data = {
            "title": "test creation"  
        }
        response = requests.post(f"{self.BASE_URL}/{self.test_todo_id}/tasksof", json=task_data)
        logging.info(f"Create Task for Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 201)  

    def test_head_tasks_for_todo(self):
        """HEAD /todos/:id/tasksof: Test headers for tasks related to a todo."""
        response = requests.head(f"{self.BASE_URL}/{self.test_todo_id}/tasksof")
        logging.info(f"Head Tasks for Todo Response: {response.status_code}")
        self.assertEqual(response.status_code, 200)

    def test_delete_task_for_todo(self):
        """DELETE /todos/:id/tasksof/:id: Test deleting a task for a todo."""
        task_data = {"title": "Test Task"}
        post_response = requests.post(f"{self.BASE_URL}/{self.test_todo_id}/tasksof", json=task_data)
        task_id = post_response.json().get("id")

        response = requests.delete(f"{self.BASE_URL}/{self.test_todo_id}/tasksof/{task_id}")
        logging.info(f"Delete Task for Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

