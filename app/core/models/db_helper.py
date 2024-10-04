from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession
from core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, pool_size: int = 5, echo: bool = False, echo_pool: bool = False,
                 max_overflow: bool = 10) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    async def dispose(self):
        """shut down the database engine"""
        await self.engine.dispose()

    async def session_getter(self):
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(
    url=str(settings.db.url),
    echo_pool=settings.db.echo_pool,
    echo=settings.db.echo,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
)
