import unittest
import requests
import logging

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

    def test_head_all_todos(self):
        """HEAD /todos: Test headers for all todos."""
        response = requests.head(self.BASE_URL)
        logging.info(f"Head All Todos Response: {response.status_code}")
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        """POST /todos: Test creating a todo."""
        todo_data = {
            "title": "New Test Todo",
            "doneStatus": False
        }
        response = requests.post(self.BASE_URL, json=todo_data)
        logging.info(f"Create Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 201)

    def test_put_todo(self):
        """PUT /todos: Test updating a todo (this is not allowed at this endpoint)."""
        todo_data = {
            "title": "Updated Test Todo",
            "doneStatus": False
        }
        response = requests.put(self.BASE_URL, json=todo_data)
        logging.info(f"Update Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

    def test_delete_todo_undocumented(self):
        """DELETE /todos: Test deleting a todo (this is not allowed at this endpoint)."""
        response = requests.delete(self.BASE_URL)
        logging.info(f"Deleting Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

    # /todos/:id
    def test_get_todo_by_id(self):
        """GET /todos/:id: Test retrieving a todo by its ID."""
        response = requests.get(f"{self.BASE_URL}/{self.test_todo_id}")
        logging.info(f"Get Todo By ID Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

    def test_head_todo_by_id(self):
        """HEAD /todos/:id: Test headers for a specific todo by its ID."""
        response = requests.head(f"{self.BASE_URL}/{self.test_todo_id}")
        logging.info(f"Head Todo By ID Response: {response.status_code}")
        self.assertEqual(response.status_code, 200)

    def test_create_todo_id(self):
        """POST /todos/:id: Test creating a todo."""
        created_data = {
            "title": "Updated Todo",
            "doneStatus": True
        }
        response = requests.put(f"{self.BASE_URL}/{self.test_todo_id}", json=created_data)
        logging.info(f"Created Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

    def test_create_todo_id_malformed_payload(self):
        """POST /todos/:id: Test creating a todo with malformed payload."""
        created_data = {
            "title": "Malformed Data Todo",
            "doneStatus": True,
            "malformedData": "test"
        }
        response = requests.put(f"{self.BASE_URL}/{self.test_todo_id}", json=created_data)
        logging.info(f"Created Todo Response with Malformed Payload: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

    def test_update_todo(self):
        """PUT /todos/:id: Test updating a todo."""
        updated_data = {
            "title": "Updated Todo",
            "doneStatus": True
        }
        response = requests.put(f"{self.BASE_URL}/{self.test_todo_id}", json=updated_data)
        logging.info(f"Update Todo Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

        response = requests.get(f"{self.BASE_URL}/{self.test_todo_id}")
        logging.info(f"Verify Updated Todo Response: {response.status_code} - {response.text}")
        todo_data = response.json().get('todos', [{}])[0]  
        self.assertEqual(todo_data["title"], "Updated Todo")

    def test_delete_todo(self):
        """DELETE /todos/:id: Test deleting a todo."""
        todo_data = {
            "title": "Temp Todo for Deletion",
            "doneStatus": False
        }
        create_response = requests.post(self.BASE_URL, json=todo_data)
        self.assertEqual(create_response.status_code, 201, "Failed to create todo for deletion test.")
        
        todo_id = create_response.json().get("id")

        response = requests.get(f"{self.BASE_URL}/{todo_id}")
        self.assertEqual(response.status_code, 200, "Todo should exist before deletion.")

        self.delete_todo(todo_id)

        response = requests.get(f"{self.BASE_URL}/{todo_id}")
        self.assertEqual(response.status_code, 404, "Todo should not exist after deletion.")

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
