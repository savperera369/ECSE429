import unittest
import requests
import logging
import time

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

    def test_create_multiple_projects(self):
        """Test creating multiple projects and measure the time."""
        num_projects = 400 
        start_time = time.time()

        for i in range(num_projects):
            project_data = {
                "title": f"Test Project {i+1}",
                "description": f"This is project {i+1}.",
                "active": True,
                "completed": False
            }
            response = requests.post(self.BASE_URL, json=project_data)
            self.assertEqual(response.status_code, 201, f"Failed to create project {i+1}")

        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"Time taken to create {num_projects} projects: {elapsed_time:.4f} seconds")

    def test_delete_multiple_projects(self):
        """Test deleting multiple projects and measure the time."""
        num_projects = 400  
        project_ids = []

        # Create multiple projects first
        for i in range(num_projects):
            project_data = {
                "title": f"Temp Project {i+1}",
                "description": f"This project will be deleted after the test.",
                "active": True,
                "completed": False
            }
            create_response = requests.post(self.BASE_URL, json=project_data)
            self.assertEqual(create_response.status_code, 201)
            project_ids.append(create_response.json().get("id"))

        # Now delete the projects
        start_time = time.time()

        for project_id in project_ids:
            response = requests.delete(f"{self.BASE_URL}/{project_id}")
            self.assertEqual(response.status_code, 200)

        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"Time taken to delete {num_projects} projects: {elapsed_time:.4f} seconds")

    def test_update_multiple_projects(self):
        """Test updating multiple projects and measure the time."""
        num_projects = 400  
        project_ids = []

        # Create multiple projects first
        for i in range(num_projects):
            project_data = {
                "title": f"Temp Project {i+1}",
                "description": f"This project will be updated.",
                "active": True,
                "completed": False
            }
            create_response = requests.post(self.BASE_URL, json=project_data)
            self.assertEqual(create_response.status_code, 201)
            project_ids.append(create_response.json().get("id"))

        # Now update the projects
        updated_data = {
            "title": "Updated Project",
            "description": "Updated description."
        }

        start_time = time.time()

        for project_id in project_ids:
            response = requests.put(f"{self.BASE_URL}/{project_id}", json=updated_data)
            self.assertEqual(response.status_code, 200)

        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"Time taken to update {num_projects} projects: {elapsed_time:.4f} seconds")

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
        """PUT /projects/:id: Test updating a project and measure the time."""
        updated_data = {
            "title": "Updated Project",
            "description": "Updated description."
        }

        start_time = time.time()  

        response = requests.put(f"{self.BASE_URL}/{self.test_project_id}", json=updated_data)

        end_time = time.time()  
        elapsed_time = end_time - start_time
        logging.info(f"Update Project Response: {response.status_code} - {response.text}")
        logging.info(f"Time taken to update Project: {elapsed_time:.4f} seconds")

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
        """DELETE /projects/:id: Test deleting a project and measure the time."""
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

        start_time = time.time()  

        self.delete_project(project_id)

        end_time = time.time()  
        elapsed_time = end_time - start_time
        logging.info(f"Time taken to delete Project: {elapsed_time:.4f} seconds")

        response = requests.get(f"{self.BASE_URL}/{project_id}")
        self.assertEqual(response.status_code, 404, "Project should not exist after deletion.")

if __name__ == "__main__":
    unittest.main()





