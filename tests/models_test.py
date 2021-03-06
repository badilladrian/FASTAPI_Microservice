import pytest
from unittest.mock import Mock
from MVC.models import (
    Yard,
    Bed,
    Plant,
    Garden,
)


class TestYard:
    # create a yard
    @pytest.mark.parametrize(
        (
            'name,'
            'expected_name'
        ), [
            ('Adrian', 'Adrian'),
            ('My first yard', 'My first yard'),
        ],
    )
    def test__init__(self, name, expected_name):
        yard = Yard(name)

        assert isinstance(yard, Yard)
        assert yard._name == expected_name

    # create a yard
    @pytest.mark.parametrize(
        (
            'name,'
            'expected_name'
        ), [
            ('Adrian', 'Adrian'),
            ('My first yard', 'My first yard'),
        ],
    )
    def test_create(self, name, expected_name):
        real = Yard(expected_name)
        mock = Mock()
        mock.name = name

        yard = real.create(mock)

        assert isinstance(yard, Yard)
        assert yard._name == expected_name

    # update a yard
    @pytest.mark.parametrize(
        (
            'id, name,'
            'expected_id, expected_name'
        ), [
            (10, 'Adrian', 10, 'Adrian'),
            (2, 'My first yard', 2, 'My first yard'),
        ],
    )
    def test_update(self, id, name, expected_id, expected_name):
        yard = Yard('test')
        mock = Mock()
        mock.id = id
        mock.name = name

        yard.update(mock)

        assert isinstance(yard, Yard)
        assert yard._id == expected_id
        assert yard._name == expected_name


class TestGarden:
    # create a garden
    @ pytest.mark.parametrize(
        (
            'name, yard_id,'
            'expected_name, expected_yard_id'
        ), [
            ('My first garden', 1, 'My first garden', 1),
            ('Front garden', None, 'Front garden', None),
        ],
    )
    def test__init__(
        self, name, yard_id,
        expected_name, expected_yard_id,
    ):
        garden = Garden(name, yard_id)

        assert isinstance(garden, Garden)
        assert garden._name == expected_name
        assert garden._yard_id == expected_yard_id

    # create a garden
    @pytest.mark.parametrize(
        (
            'name, yard_id,'
            'expected_name, expected_yard_id'
        ), [
            ('My first garden', 1, 'My first garden', 1),
            ('Front garden', None, 'Front garden', None),
        ],
    )
    def test_create(
        self, name, yard_id,
        expected_name, expected_yard_id,
    ):
        real = Garden(expected_name, expected_yard_id)
        mock = Mock()
        mock.name = name
        mock.yard_id = yard_id

        garden = real.create(mock)

        assert isinstance(garden, Garden)
        assert garden._name == expected_name
        assert garden._yard_id == expected_yard_id

    # update a garden
    @pytest.mark.parametrize(
        (
            'id, name, yard_id,'
            'expected_id, expected_name, expected_yard_id'
        ), [
            (10, 'My Garden', 10, 10, 'My Garden', 10),
            (2, 'Adrian', 2, 2, 'Adrian', 2),
        ],
    )
    def test_update(
        self, id, name, yard_id,
        expected_id, expected_name, expected_yard_id,
    ):
        garden = Garden('test', 1)
        mock = Mock()
        mock.id = id
        mock.name = name
        mock.yard_id = yard_id

        garden.update(mock)

        assert isinstance(garden, Garden)
        assert garden._id == expected_id
        assert garden._name == expected_name
        assert garden._yard_id == expected_yard_id


class TestBed:
    # create a bed
    @ pytest.mark.parametrize(
        'name, yard_id, garden_id,'
        'expected_name, expected_yard_id, expected_garden_id', [
            ('My bed', 1, None, 'My bed', 1, None),
            ('Your bed', 8234, 1, 'Your bed', 8234, 1),
        ],
    )
    def test_init__(
            self, name, yard_id, garden_id,
            expected_name, expected_yard_id, expected_garden_id,
    ):
        bed = Bed(name, yard_id, garden_id)

        assert isinstance(bed, Bed)

        assert bed._name == expected_name
        assert bed._yard_id == expected_yard_id
        assert bed._garden_id == expected_garden_id

    # create a bed
    @pytest.mark.parametrize(
        'name, yard_id, garden_id,'
        'expected_name, expected_yard_id, expected_garden_id', [
            ('My bed', 1, 1, 'My bed', 1, 1),
            ('Your bed', 8234, None, 'Your bed', 8234, None),
        ],
    )
    def test_create(
            self, name, yard_id, garden_id,
            expected_name, expected_yard_id, expected_garden_id,
    ):
        real = Bed(expected_name, expected_yard_id, expected_garden_id)
        mock = Mock()
        mock.name = name
        mock.yard_id = yard_id
        mock.garden_id = garden_id

        bed = real.create(mock)

        assert isinstance(bed, Bed)
        assert bed._name == expected_name
        assert bed._yard_id == expected_yard_id
        assert bed._garden_id == expected_garden_id

    # update a bed
    @pytest.mark.parametrize(
        (
            'id, name, yard_id, garden_id,'
            'expected_id, expected_name, expected_yard_id, expected_garden_id'
        ), [
            (10, 'My bed', 1, 1, 10, 'My bed', 1, 1),
            (2, None, None, None, 2, 'test', 1, None),
        ],
    )
    def test_update(
        self, id, name, yard_id, garden_id,
        expected_id, expected_name, expected_yard_id, expected_garden_id,
    ):
        bed = Bed('test', 1)
        mock = Mock()
        mock.id = id
        mock.name = name
        mock.yard_id = yard_id
        mock.garden_id = garden_id

        bed.update(mock)

        assert isinstance(bed, Bed)
        assert bed._id == expected_id
        assert bed._name == expected_name
        assert bed._yard_id == expected_yard_id
        assert bed._garden_id == expected_garden_id


class TestPlant:
    # create a plant
    @ pytest.mark.parametrize(
        (
            'name, bed_id,'
            'expected_name, expected_bed_id'
        ), [
            ('Cillantro', 1, 'Cillantro', 1),
            ('Beans', 2, 'Beans', 2),
        ],
    )
    def test__init__(
        self, name, bed_id,
        expected_name, expected_bed_id,
    ):
        plant = Plant(name, bed_id)

        assert isinstance(plant, Plant)
        assert plant._name == expected_name
        assert plant._bed_id == expected_bed_id

    # create a plant
    @pytest.mark.parametrize(
        (
            'name, bed_id,'
            'expected_name, expected_bed_id'
        ), [
            ('Cillantro', 1, 'Cillantro', 1),
            ('Beans', 2, 'Beans', 2),
        ],
    )
    def test_create(
        self, name, bed_id,
        expected_name, expected_bed_id,
    ):
        real = Plant(expected_name, expected_bed_id)
        mock = Mock()
        mock.name = name
        mock.bed_id = bed_id

        plant = real.create(mock)

        assert isinstance(plant, Plant)
        assert plant._name == expected_name
        assert plant._bed_id == expected_bed_id

    # update a plant
    @pytest.mark.parametrize(
        (
            'id, name, bed_id,'
            'expected_id, expected_name, expected_bed_id'
        ), [
            (10, 'Cillantro', 10, 10, 'Cillantro', 10),
            (2, 'Beans', 2, 2, 'Beans', 2),
        ],
    )
    def test_update(
        self, id, name, bed_id,
        expected_id, expected_name, expected_bed_id,
    ):
        plant = Plant('test', 1)
        mock = Mock()
        mock.id = id
        mock.name = name
        mock.bed_id = bed_id

        plant.update(mock)

        assert isinstance(plant, Plant)
        assert plant._id == expected_id
        assert plant._name == expected_name
        assert plant._bed_id == expected_bed_id
