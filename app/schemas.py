from pydantic import BaseModel, ConfigDict, Field, field_validator
import typing


class TaskCreate(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    status: typing.Literal["todo", "in_progress", "done"] = "todo"


class TaskUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    status: typing.Literal["todo", "in_progress", "done"] | None = None

    @field_validator("title", "status", mode="before")
    @classmethod
    def reject_null_updates(cls, value: typing.Any) -> typing.Any:
        if value is None:
            raise ValueError("Field cannot be null")
        return value


class Task(TaskCreate):
    id: int