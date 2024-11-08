from flask_restful import Resource
from werkzeug.exceptions import NotFound

from db import db
from models.exercise import ExerciseModel
from models.program import ProgramModel


class ProgramManager(Resource):
    @staticmethod
    def create_program(program_data):
        exercise_data = program_data.pop("exercises", [])
        program = ProgramModel(**program_data)

        exercises = []
        for exercise in exercise_data:
            exercise_instance = db.session.query(ExerciseModel).filter_by(pk=exercise["pk"]).scalar()
            if not exercise_instance:
                raise NotFound(f"Exercise with pk={exercise['pk']} does not exist")
            exercises.append(exercise_instance)

        program.exercises = exercises
        db.session.add(program)
        db.session.flush()
        return program

    @staticmethod
    def get_all_programs():
        return db.session.execute(db.select(ProgramModel)).scalars().all()

    @staticmethod
    def get_program(program_pk):
        program = db.session.execute(db.select(ProgramModel).filter_by(pk=program_pk)).scalar_one_or_none()
        if program is None:
            raise NotFound
        return program
