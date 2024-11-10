from flask_restful import Resource

from managers.trainer import TrainerManager


class CreateTrainer(Resource):
    def put(self, user_pk):
        TrainerManager.change_role(user_pk)
        return 204
