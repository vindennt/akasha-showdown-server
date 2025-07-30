# Code adapted from https://github.com/AtticusZeller/fastapi_supabase_template/
from collections.abc import Generator

from sqlmodel import Session, create_engine, select
from supabase import create_client, Client

from app.core.config import settings
# TODO: add User model
from app.db.models import *

# TODO: Ensure all SQLModel models are imported (app.models) before DB init
# to avoid issues with relationships not registering properly:
# https://github.com/fastapi/full-stack-fastapi-template/issues/28

engine = create_engine(str(settings.DATABASE_URL))

def get_db() -> Generator[Session, None]:
    with Session(engine) as session:
        yield session


def init_db(session: Session) -> None:
    # TODO: Create tabless with Alembic
    result = session.exec(select(User).where(User.email == settings.FIRST_SUPERUSER))
    user = result.first()

    if not user:
        super_client: Client = create_client(settings.DATABASE_URL, settings.DATABASE_KEY)

        response = super_client.auth.sign_up(
            {
                "email": settings.FIRST_SUPERUSER,
                "password": settings.FIRST_SUPERUSER_PASSWORD,
            }
        )
        assert response.user.email == settings.FIRST_SUPERUSER
        assert response.user.id is not None
        assert response.session.access_token is not None
