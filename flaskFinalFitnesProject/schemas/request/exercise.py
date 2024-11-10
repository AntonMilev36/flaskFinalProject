from marshmallow import Schema, validate, fields

from utils.validators import validate_name


class CreateExerciseRequest(Schema):
    name = fields.String(required=True, validate=validate.And(validate.Length(min=4, max=50)))
    description = fields.String(required=True, validate=validate.And(validate.Length(min=50)))
    tutorial_photo = fields.String(required=True)
    tutorial_extension = fields.String(required=True)
    video_example = fields.String(required=True)  # Поле за видео в Base64
    video_extension = fields.String(required=True)
    author = fields.String(required=True, validate=validate_name)


class ExerciseProgramRequest(Schema):
    pk = fields.Integer(required=True)
