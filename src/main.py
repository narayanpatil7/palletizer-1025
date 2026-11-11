import asyncio

from viam.module.module import Module
from models.palletizer import Palletizer


async def main():
    module = Module.from_args()

    module.add_model_from_registry(
        Palletizer.API,
        Palletizer.MODEL,
    )

    await module.start()


if __name__ == "__main__":
    asyncio.run(main())
