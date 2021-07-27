from typing import List, Optional

from MVC.models import (
    Bed,
    BedRequestCreate,
    BedRequestUpdate,
    Plant,
    PlantRequestCreate,
    PlantRequestUpdate,
    Yard,
    YardRequestCreate,
    YardRequestUpdate,
)

from utils.db import session


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
        return session.query(Yard).all()

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
        return session.query(Yard).get(id)

    def create(self, request: List[YardRequestCreate]) -> List[Yard]:
        """
            This method creates one or more yards, 

        Args:
            request(List[YardRequestCreate]): list of YardRequestCreate objects per each Yard that is going to be created
        Returns:
            List[Yard]: list containing all the yards created
        Raises:
            None
        """
        self._yards = [Yard.create(yard) for yard in request]
        session.add_all(self._yards)
        session.commit
        return self._yards

    def delete(self, id) -> bool:
        """
            This method deletes one yard, 

        Args:
            id(int): corresponding yard's id for the one that is going to be deleted
        Returns:
            bool: if deletetion was successfully execuded
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

    def update(self, id: int, request: YardRequestUpdate) -> bool:
        """
            This method updates one yard, 

        Args:
            id(int): corresponding yard's id for the one that is going to be updated
            request(YardRequestUpdate): Request containing the new values
        Returns:
            bool: if update was successfully execuded
        Raises:
            None
        """
        result = False
        yard = self.get_one(id)
        if yard:
            yard.update(request)
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
        beds: List[Bed] = []
        if (request):
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
            List[Yard]: list of all the existing beds
        Raises:
            None
        """
        return session.query(Bed).all()

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
        return session.query(Bed).get(id)

    def create(self, request: list[BedRequestCreate]) -> list[Bed]:
        """
            This method creates one or more beds, 

        Args:
            request(List[BedRequestCreate]): list of a BedRequestCreate object per each Bed that is going to be created
        Returns:
            List[Bed]: list containing all the beds created
        Raises:
            None
        """
        self._beds = [Bed.create(bed) for bed in request]
        session.add_all(self._beds)
        session.commit
        return self._beds

    def delete(self, id) -> bool:
        """
            This method deletes one bed, 

        Args:
            id(int): corresponding bed's id for the one that is going to be deleted
        Returns:
            bool: if deletetion was successfully execuded
        Raises:
            None
        """
        result = False
        bed = self.get_one(id)
        if bed:
            session.delete(bed)
            session.commit
            result = True
        return result

    def update(self, id: int, request: BedRequestUpdate) -> bool:
        """
            This method updates one bed, 

        Args:
            id(int): corresponding bed's id for the one that is going to be updated
            request(BedRequestUpdate): Request containing the new values
        Returns:
            bool: if update was successfully execuded
        Raises:
            None
        """
        result = False
        bed = self.get_one(id)
        if (bed):
            bed.update(request)
            session.commit()
            result = True
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
        return session.query(Plant).get(id)

    def create(self, request: list[PlantRequestCreate]) -> list[Plant]:
        """
            This method creates one or more plants, 

        Args:
            request(List[PlantRequestCreate]): list of a PlantRequestCreate object per each Plant that is going to be created
        Returns:
            List[Plant]: list containing all the plants created
        Raises:
            None
        """
        self._beds = [Plant.create(bed) for bed in request]
        session.add_all(self._beds)
        session.commit
        return self._beds

    def delete(self, id) -> bool:
        """
            This method deletes one plant, 

        Args:
            id(int): corresponding plant's id for the one that is going to be deleted
        Returns:
            bool: if deletetion was successfully execuded
        Raises:
            None
        """
        result = False
        plant = self.get_one(id)
        if plant:
            session.delete(plant)
            session.commit
            result = True
        return result

    def update(self, id: int, request: PlantRequestUpdate) -> bool:
        """
            This method updates one plant, 

        Args:
            id(int): corresponding plant's id for the one that is going to be updated
            request(PlantRequestUpdate): Request containing the new values
        Returns:
            bool: if update was successfully execuded
        Raises:
            None
        """
        result = False
        plant = self.get_one(id)
        if (plant):
            plant.update(request)
            session.commit()
            result = True
        return result
