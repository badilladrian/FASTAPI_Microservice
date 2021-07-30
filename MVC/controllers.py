from typing import List, Optional
import logging

from MVC.models import (
    Bed,
    BedRequestCreate,
    BedRequestUpdate,
    Garden,
    GardenRequestCreate,
    GardenRequestUpdate,
    Plant,
    PlantRequestCreate,
    PlantRequestUpdate,
    Yard,
    YardRequestCreate,
    YardRequestUpdate,
)

from utils.db import session

# Setting logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s:%(name)s-%(levelname)ss:%(message)s")
file_handler = logging.FileHandler("logs/controllers.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class ControllerYards:
    _yards: List[Yard] = []

    def __init__(self) -> None:
        """
            Create a new yard's controller.

        Args:
            None
        Returns:
            None
        Raises:
            None
        """
        logger.debug("Executing ControllerYards __init__")
        self._yards = self.get_all()

    def get_multi(self, request: Optional[List[int]] = None) -> List[Yard]:
        """
            This method returns from 1 to all the existing yards,

        Args:
            request(Optional[List[int]]): List of the yard's ids
        Returns:
            List[Yard]: list of all the found yards
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerYards get_multi with the following request param: {request}")
        yards: List[Yard] = []
        if (request):
            for id in request:
                yard = self.get_one(id)
                if (yard):
                    yards.append(yard)
        else:
            yards = self.get_all()
        return yards

    def get_all(self) -> List[Yard]:
        """
            This method returns all the existing yards,

        Args:
            None
        Returns:
            List[Yard]: list of all the existing yards
        Raises:
            None
        """
        logger.debug("Executing ControllerYards get_all")
        try:
            logger.debug("Quering database, fetching all Yards")
            yards = session.query(Yard).all()
            if yards:
                logger.info("Query successfully executed")
                return yards
            else:
                logger.warning("There are no yards at the database")
        except Exception:
            logger.exception("Query was not executed")

    def get_one(self, id) -> Yard:
        """
            This method returns one yard,

        Args:
            id(id): the corresponding yard's id
        Returns:
            Yard: corresponding Yard object
        Raises:
            None
        """
        logger.debug(f"Executing ControllerYards get_one with id: {id}")
        try:
            yard = session.query(Yard).get(id)
            if yard:
                logger.info(f"Yard {yard.__repr__()}, successfuly found")
                return yard
            else:
                logger.warning(f"Yard: {id} not found")
        except Exception:
            logging.exception("Query was not executed")

    def create(self, request: List[YardRequestCreate]) -> List[Yard]:
        """
            This method creates one or more yards,

        Args:
            request(List[YardRequestCreate]):
                list of YardRequestCreate objects
                per each Yard that is going to be created
        Returns:
            List[Yard]: list containing all the yards created
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerYards create with request: {request}")
        try:
            self._yards = [Yard.create(yard) for yard in request]
            if self._yards:
                logger.debug(
                    f"Query to database, create yards")
                session.add_all(self._yards)
                session.commit
                logger.info("Yards successfuly created")

            else:
                logger.warning("Yards not created")
        except Exception:
            logging.exception("Query was not executed")

    def delete(self, id) -> bool:
        """
            This method deletes one yard,

        Args:
            id(int):
                corresponding yard's id for the one that is going to be deleted
        Returns:
            bool: if deletetion was successfully execuded
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerYards delete with id: {id}")
        result = False
        yard = self.get_one(id)
        if yard:
            try:
                logger.debug(
                    f"Query to datase delete with id: {id}")
                session.delete(yard)
                session.commit
                result = True
                logger.info(f"Yards successfuly deleted")
            except Exception:
                logging.exception("Query was not executed")
        return result

    def update(self, id: int, request: YardRequestUpdate) -> bool:
        """
            This method updates one yard
        Args:
            id(int):
                corresponding yard's id
                for the one that is going to be updated
            request(YardRequestUpdate):
                Request containing the new values
        Returns:
            bool: if update was successfully execuded
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerYards update with id: {id}")
        result = False
        yard = self.get_one(id)
        if yard:
            try:
                logger.debug(
                    f"Query to datase update yard: {id}")
                yard.update(request)
                session.commit()
                result = True
                logger.info(f"Yard successfuly updated")
            except Exception:
                logging.exception("Query was not executed")
        return result


class ControllerGardens:
    _gardens: List[Garden] = []

    def __init__(self) -> None:
        """
            Create a new garden's controller.

        Args:
            None
        Returns:
            None
        Raises:
            None
        """
        self._gardens = self.get_all()

    def get_multi(self, request: Optional[List[int]] = None) -> List[Garden]:
        """
            This method returns from 1 to all the existing gardens,

        Args:
            request(Optional[List[int]]): List of the garden's ids
        Returns:
            List[Garden]: list of all the found garden
        Raises:
            None
        """
        gardens: List[Garden] = []
        if (request):
            for id in request:
                garden = self.get_one(id)
                if (garden):
                    gardens.append(garden)
        else:
            gardens = self.get_all()
        return gardens

    def get_all(self) -> List[Garden]:
        """
            This method returns all the existing gardens,

        Args:
            None
        Returns:
            List[Garden]: list of all the existing gardens
        Raises:
            None
        """
        return session.query(Garden).all()

    def get_one(self, id) -> Garden:
        """
            This method returns one garden,

        Args:
            id(id): the corresponding garden's id
        Returns:
            Garden: corresponding Garden object
        Raises:
            None
        """
        return session.query(Garden).get(id)

    def create(self, request: List[GardenRequestCreate]) -> List[Garden]:
        """
            This method creates one or more gardens
        Args:
            request(List[GardenRequestCreate]):
                list of GardenRequestCreate objects
                per each Garden that is going to be created
        Returns:
            List[Garden]:
                list containing all the gardens created
        Raises:
            None
        """
        self._gardens = [Garden.create(garden) for garden in request]
        session.add_all(self._gardens)
        session.commit
        return self._gardens

    def delete(self, id) -> bool:
        """
            This method deletes one garden
        Args:
            id(int):
                corresponding garden's id for
                the one that is going to be deleted
        Returns:
            bool:
                if deletetion was successfully execuded
        Raises:
            None
        """
        result = False
        yard = self.get_one(id)
        if yard:
            session.delete(yard)
            session.commit
            result = True
        return result

    def update(self, id: int, request: GardenRequestUpdate) -> bool:
        """
            This method updates one garden
        Args:
            id(int):
                corresponding garden's id
                for the one that is going to
                be updated
            request(GardenRequestUpdate):
                Request containing the new values
        Returns:
            bool:
                if update was successfully execuded
        Raises:
            None
        """
        result = False
        garden = self.get_one(id)
        if garden:
            garden.update(request)
            session.commit()
            result = True
        return result


class ControllerBeds:
    _beds: List[Bed] = []

    def __init__(self) -> None:
        """
            Create a new bed's controller.

        Args:
            None
        Returns:
            None
        Raises:
            None
        """
        logger.debug(
            "Executing ControllerBeds __init__()")
        self._beds = self.get_all()

    def get_multi(self, request: Optional[List[int]] = None) -> List[Bed]:
        """
            This method returns from 1 to all the existing beds,

        Args:
            request(Optional[List[int]]): List of the bed's ids
        Returns:
            List[Bed]: list of all the found beds
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerBeds get_multi with request: {request}")
        beds: List[Bed] = []
        if request:
            for id in request:
                bed = self.get_one(id)
                if (bed):
                    beds.append(bed)
        else:
            beds = self.get_all()
        return beds

    def get_all(self) -> List[Bed]:
        """
            This method returns all the existing beds,

        Args:
            None
        Returns:
            List[Bed]: list of all the existing beds
        Raises:
            None
        """
        logger.debug(
            "Executing ControllerBeds get_all")
        try:
            logger.debug("Quering database, fetching all beds")
            beds = session.query(Bed).all()
            if beds:
                logger.info("Query successfully executed")
                return beds
            else:
                logger.warning("There are no beds at the database")
        except Exception:
            logger.exception("Query was not executed")

        return beds

    def get_one(self, id: int) -> Bed:
        """
            This method returns one bed,

        Args:
            id(id): the corresponding bed's id
        Returns:
            Bed: corresponding Bed object
        Raises:
            None
        """
        logger.debug(f"Executing ControllerBeds get_one with id: {id}")
        try:
            bed = session.query(Bed).get(id)
            if bed:
                logger.info(f"Bed {bed.__repr__()}, successfuly found")
                return bed
            else:
                logger.warning(f"Bed: {id} not found")
        except Exception:
            logging.exception("Query was not executed")
        return bed

    def create(self, request: list[BedRequestCreate]) -> list[Bed]:
        """
            This method creates one or more beds
        Args:
            request(List[BedRequestCreate]):
                list of a BedRequestCreate object per
                each Bed that is going to be created
        Returns:
            List[Bed]:
                list containing all the beds created
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerBeds create with request: {request}")
        try:
            self._beds = [Bed.create(bed) for bed in request]
            if self._beds:
                logger.debug(
                    f"Query to database, create beds")
                session.add_all(self._beds)
                session.commit
                logger.info("Beds successfuly created")

            else:
                logger.warning("Beds not created")
        except Exception:
            logging.exception("Query was not executed")
        return self._beds

    def delete(self, id) -> bool:
        """
            This method deletes one bed
        Args:
            id(int):
                corresponding bed's id for
                the one that is going to be deleted
        Returns:
            bool:
                if deletetion was successfully execuded
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerBeds delete with id: {id}")
        result = False
        bed = self.get_one(id)
        if bed:
            try:
                logger.debug(
                    f"Query to datase delete with id: {id}")
                session.delete(bed)
                session.commit
                result = True
                logger.info(f"Beds successfuly deleted")
            except Exception:
                logging.exception("Query was not executed")
        return result

    def update(self, id: int, request: BedRequestUpdate) -> bool:
        """
            This method updates one bed
        Args:
            id(int):
                corresponding bed's id for the one that is going to be updated
            request(BedRequestUpdate):
                Request containing the new values
        Returns:
            bool: if update was successfully execuded
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerBeds update with id: {id}")
        result = False
        bed = self.get_one(id)
        if bed:
            try:
                logger.debug(
                    f"Query to datase update bed: {id}")
                bed.update(request)
                session.commit()
                result = True
                logger.info(f"Bed successfuly updated")
            except Exception:
                logging.exception("Query was not executed")
        return result


class ControllerPlants:
    _plants: List[Plant] = []

    def __init__(self) -> None:
        """
            Create a new plant's controller.

        Args:
            None
        Returns:
            None
        Raises:
            None
        """
        self._plants = self.get_all()

    def get_multi(self, request: Optional[List[int]] = None) -> List[Plant]:
        """
            This method returns from 1 to all the existing plants,

        Args:
            request(Optional[List[int]]): List of the plant's ids
        Returns:
            List[Plant]: list of all the found plants
        Raises:
            None
        """
        plants: List[Plant] = []
        if (request):
            for id in request:
                plant = self.get_one(id)
                if (plant):
                    plants.append(plant)
        else:
            plants = self.get_all()
        return plants

    def get_all(self) -> List[Plant]:
        """
            This method returns all the existing plants,

        Args:
            None
        Returns:
            List[Plant]: list of all the existing plants
        Raises:
            None
        """
        return session.query(Plant).all()

    def get_one(self, id: int) -> Plant:
        """
            This method returns one plant,

        Args:
            id(id): the corresponding plant's id
        Returns:
            Plant: corresponding Plant object
        Raises:
            None
        """
        logger.debug(f"Executing ControllerPlants get_one with id: {id}")
        try:
            plant = session.query(Plant).get(id)
            if plant:
                logger.info(f"Plant {plant.__repr__()}, successfuly found")
                return plant
            else:
                logger.warning(f"Plant: {id} not found")
        except Exception:
            logging.exception("Query was not executed")
        return plant

    def create(self, request: list[PlantRequestCreate]) -> list[Plant]:
        """
            This method creates one or more plants,

        Args:
            request(List[PlantRequestCreate]):
                list of a PlantRequestCreate object per
                each Plant that is going to be created
        Returns:
            List[Plant]:
                list containing all the plants created
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerPlants create with request: {request}")
        try:
            self._plants = [Plant.create(plant) for plant in request]
            if self._plants:
                logger.debug(
                    f"Query to database, create plants")
                session.add_all(self._plants)
                session.commit
                logger.info("Plants successfuly created")

            else:
                logger.warning("Plants not created")
        except Exception:
            logging.exception("Query was not executed")
        return self._plants

    def delete(self, id) -> bool:
        """
            This method deletes one plant
        Args:
            id(int):
                corresponding plant's id
                for the one that is going to be deleted
        Returns:
            bool:
                if deletetion was successfully execuded
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerPlants delete with id: {id}")
        result = False
        plant = self.get_one(id)
        if plant:
            try:
                logger.debug(
                    f"Query to datase delete with id: {id}")
                session.delete(plant)
                session.commit
                result = True
                logger.info(f"Plants successfuly deleted")
            except Exception:
                logging.exception("Query was not executed")

    def update(self, id: int, request: PlantRequestUpdate) -> bool:
        """
            This method updates one plant
        Args:
            id(int):
                corresponding plant's id for
                the one that is going to be updated
            request(PlantRequestUpdate):
                Request containing the new values
        Returns:
            bool: if update was successfully execuded
        Raises:
            None
        """
        logger.debug(
            f"Executing ControllerPlants update with id: {id}")
        result = False
        plant = self.get_one(id)
        if plant:
            try:
                logger.debug(
                    f"Query to datase update plant: {id}")
                plant.update(request)
                session.commit()
                result = True
                logger.info(f"Plant successfuly updated")
            except Exception:
                logging.exception("Query was not executed")
        return result
