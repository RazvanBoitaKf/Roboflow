from roboflow import Roboflow

class RoboflowHandler:
    def __init__(self, project_id):
        self.project_id = project_id
        self.rf = Roboflow(api_key="3N9lBuccbpGSuITSmuP8")
        self.workspace = self.rf.workspace()
        self.project = self.workspace.project(self.project_id)

    def get_our_project(self):
        return self.project
    
    def upload_dataset(self, dataset_path):
        self.workspace.upload_dataset(
            dataset_path,
            project_name=self.project_id
        )

    def generate_version(self, settings):
        new_version = self.project.generate_version(settings=settings)
        return self.project.version(new_version)

    def train_model(self, version):
        model = version.train(
            speed="fast",
            checkpoint=None,
            plot_in_notebook=False 
        )
        return model
