import pytest
from unittest.mock import Mock
from MVC.models import Yard, Bed, Plant


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
    def test_init__(self, name, expected_name):
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


class TestBed:
    # create a bed
    @ pytest.mark.parametrize(
        'yard_id, expected_yard_id', [
            (1, 1),
            (8234, 8234),
        ],
    )
    def test_init__(self, yard_id, expected_yard_id):
        bed = Bed(yard_id)

        assert isinstance(bed, Bed)
        assert bed._yard_id == expected_yard_id

    # create a bed
    @pytest.mark.parametrize(
        'yard_id, expected_yard_id', [
            (1, 1),
            (8234, 8234),
        ],
    )
    def test_create(self, yard_id, expected_yard_id):
        real = Bed(expected_yard_id)
        mock = Mock()
        mock.yard_id = yard_id

        bed = real.create(mock)

        assert isinstance(bed, Bed)
        assert bed._yard_id == expected_yard_id

    # update a bed
    @pytest.mark.parametrize(
        (
            'id, yard_id,'
            'expected_id, expected_yard_id'
        ), [
            (10, 20, 10, 20),
            (2, 1, 2, 1),
        ],
    )
    def test_update(
        self, id, yard_id,
        expected_id, expected_yard_id,
    ):
        bed = Bed(5)
        mock = Mock()
        mock.id = id
        mock.yard_id = yard_id

        bed.update(mock)

        assert isinstance(bed, Bed)
        assert bed._id == expected_id
        assert bed._yard_id == expected_yard_id


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
            'id, name, bed_id'
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
