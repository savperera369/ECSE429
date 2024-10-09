import unittest
import requests
import logging

logging.basicConfig(level=logging.INFO)

class TestTodoManagerAPI(unittest.TestCase):
    BASE_URL = "http://localhost:4567/projects"
    
    def setUp(self):
        """Set up the initial state before each test."""
        self.test_project_id = self.create_test_project()

    def tearDown(self):
        """Clean up after each test."""
        if self.test_project_id:
            self.delete_project(self.test_project_id)

    def create_test_project(self):
        """Create a test project and return its ID."""
        project_data = {
            "title": "Test Project",
            "description": "This is a test project.",
            "active": True,
            "completed": False
        }
        response = requests.post(self.BASE_URL, json=project_data)
        logging.info(f"Create Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 201)
        return response.json().get("id")

    def delete_project(self, project_id):
        """Delete a project by its ID."""
        response = requests.delete(f"{self.BASE_URL}/{project_id}")
        logging.info(f"Delete Project Response: {response.status_code} - {response.text}")
        self.assertIn(response.status_code, [204, 200])

    # /projects
    def test_get_all_projects(self):
        """GET /projects: Test retrieving all projects."""
        response = requests.get(self.BASE_URL)
        logging.info(f"Get All Projects Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json().get('projects'), list)

    def test_head_all_projects(self):
        """HEAD /projects: Test headers for all projects."""
        response = requests.head(self.BASE_URL)
        logging.info(f"Head All Projects Response: {response.status_code}")
        self.assertEqual(response.status_code, 200)

    def test_create_project(self):
        """POST /projects: Test creating a project."""
        project_data = {
            "title": "New Test Project",
            "description": "This is a new test project.",
            "active": True,
            "completed": False
        }
        response = requests.post(self.BASE_URL, json=project_data)
        logging.info(f"Create Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 201)

    def test_create_project_malformed_payload(self):
        """POST /projects: Test creating a project with a malformed payload."""
        project_data = {
            "title": "New Test Project",
            "description": "This is a new test project.",
            "active": True,
            "completed": False,
            "malformed": "malformed"
        }
        response = requests.post(self.BASE_URL, json=project_data)
        logging.info(f"Create Project Response with Malformed Payload: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 400)

    def test_put_project_id(self):
        """PUT /projects/:id: Test updating a project (this is not allowed at this endpoint)."""
        updated_data = {
            "title": "Updated Project",
            "description": "Updated description."
        }
        response = requests.put(self.BASE_URL, json=updated_data)
        logging.info(f"Update Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 405)

    # /projects/:id
    def test_get_project_by_id(self):
        """GET /projects/:id: Test retrieving a project by its ID."""
        response = requests.get(f"{self.BASE_URL}/{self.test_project_id}")
        logging.info(f"Get Project By ID Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)
        project_data = response.json().get('projects', [{}])[0]
        self.assertIn("title", project_data)

    def test_head_project_by_id(self):
        """HEAD /projects/:id: Test headers for a specific project by its ID."""
        response = requests.head(f"{self.BASE_URL}/{self.test_project_id}")
        logging.info(f"Head Project By ID Response: {response.status_code}")
        self.assertEqual(response.status_code, 200)

    def test_update_project(self):
        """PUT /projects/:id: Test updating a project."""
        updated_data = {
            "title": "Updated Project",
            "description": "Updated description."
        }
        response = requests.put(f"{self.BASE_URL}/{self.test_project_id}", json=updated_data)
        logging.info(f"Update Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

        response = requests.get(f"{self.BASE_URL}/{self.test_project_id}")
        logging.info(f"Verify Updated Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)
        project_data = response.json().get('projects', [{}])[0]
        self.assertEqual(project_data["title"], "Updated Project")

    def test_create_project_id(self):
        """POST /projects/:id: Test creating a project."""
        created_data = {
            "title": "New Project",
            "description": "New description."
        }
        response = requests.put(f"{self.BASE_URL}/{self.test_project_id}", json=created_data)
        logging.info(f"Create Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

    def test_delete_project(self):
        """DELETE /projects/:id: Test deleting a project."""
        
        project_data = {
            "title": "Temp Project for Deletion",
            "description": "This project will be deleted after the test.",
            "active": True,
            "completed": False
        }
        create_response = requests.post(self.BASE_URL, json=project_data)
        self.assertEqual(create_response.status_code, 201, "Failed to create project for deletion test.")
        
        project_id = create_response.json().get("id")

        response = requests.get(f"{self.BASE_URL}/{project_id}")
        self.assertEqual(response.status_code, 200, "Project should exist before deletion.")

        self.delete_project(project_id)

        response = requests.get(f"{self.BASE_URL}/{project_id}")
        self.assertEqual(response.status_code, 404, "Project should not exist after deletion.")

    # /projects/:id/tasks
    def test_create_task_for_project(self):
        """POST /projects/:id/tasks: Test creating a task for a project."""
        task_data = {
            "title": "test"
        }
        response = requests.post(f"{self.BASE_URL}/{self.test_project_id}/tasks", json=task_data)
        logging.info(f"Create Task for Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 201)

    def test_get_tasks_for_project(self):
        """GET /projects/:id/tasks: Test retrieving tasks for a project."""
        response = requests.get(f"{self.BASE_URL}/{self.test_project_id}/tasks")
        logging.info(f"Get Tasks for Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json().get('todos'), list)

    def test_head_tasks_for_project(self):
        """HEAD /projects/:id/tasks: Test headers for tasks related to a project."""
        response = requests.head(f"{self.BASE_URL}/{self.test_project_id}/tasks")
        logging.info(f"Head Tasks for Project Response: {response.status_code}")
        self.assertEqual(response.status_code, 200)

    def test_delete_task_for_project(self):
        """DELETE /projects/:id/tasks/:id: Test deleting a task for a project."""
        task_data = {"title": "Test Task"}
        post_response = requests.post(f"{self.BASE_URL}/{self.test_project_id}/tasks", json=task_data)
        task_id = post_response.json().get("id")

        response = requests.delete(f"{self.BASE_URL}/{self.test_project_id}/tasks/{task_id}")
        logging.info(f"Delete Task for Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

    # /projects/:id/categories
    def test_create_category_for_project(self):
        """POST /projects/:id/categories: Test creating a category for a project."""
        category_data = {
            "title": "Test Category"
        }
        response = requests.post(f"{self.BASE_URL}/{self.test_project_id}/categories", json=category_data)
        logging.info(f"Create Category for Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 201)

    def test_get_categories_for_project(self):
        """GET /projects/:id/categories: Test retrieving categories for a project."""
        response = requests.get(f"{self.BASE_URL}/{self.test_project_id}/categories")
        logging.info(f"Get Categories for Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json().get('categories'), list)

    def test_head_categories_for_project(self):
        """HEAD /projects/:id/categories: Test headers for categories related to a project."""
        response = requests.head(f"{self.BASE_URL}/{self.test_project_id}/categories")
        logging.info(f"Head Categories for Project Response: {response.status_code}")
        self.assertEqual(response.status_code, 200)

    def test_delete_category_for_project(self):
        """DELETE /projects/:id/categories/:id: Test deleting a category for a project."""
        category_data = {"title": "Test Category"}
        post_response = requests.post(f"{self.BASE_URL}/{self.test_project_id}/categories", json=category_data)
        category_id = post_response.json().get("id")

        response = requests.delete(f"{self.BASE_URL}/{self.test_project_id}/categories/{category_id}")
        logging.info(f"Delete Category for Project Response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()




