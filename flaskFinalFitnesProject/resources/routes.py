from resources.auth import RegisterUser, LoginUser
from resources.exercise import CreateExercise, AllExercisesList, SpecificExercise
from resources.payment import InitiatePayment, PaymentSuccess, PaymentCancel
from resources.program import CreateProgram, AllProgramsList, SpecificProgram
from resources.user import AddProgramToUser, UserProgramsList, UserSpecificProgram

routes = (
    (RegisterUser, "/register"),
    (LoginUser, "/login"),
    (CreateExercise, "/trainers/exercise"),
    (CreateProgram, "/trainers/program"),
    (AllExercisesList, "/exercise"),
    (AllProgramsList, "/program"),
    (SpecificExercise, "/exercise/<int:exercise_pk>"),
    (SpecificProgram, "/program/<int:program_pk>"),
    (AddProgramToUser, "/users/add/program/<int:program_pk>"),
    (UserProgramsList, "/user/program"),
    (UserSpecificProgram, "/user/program/<int:program_pk>"),
    (InitiatePayment, "/user/payment"),
    (PaymentSuccess, "/success"),
    (PaymentCancel, "/cancel"),
)
