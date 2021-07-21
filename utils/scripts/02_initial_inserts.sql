\c farmly;

INSERT INTO public.entry_groups("group")
VALUES ('Observe'),
      ('Action'),
      ('Eat');

INSERT INTO public.entry_types("type","entry_group_id")
VALUES('General',1),
      ('Life-cycle',1),
      ('Measure',1),
      ('Calamity',1),
      ('Timelapse',1),
      ('Weather',1),
      ('Sensors',1),
      ('General',2),
      ('Weeding',2),
      ('Transplanting',2),
      ('Amend',2),
      ('Hand Watering',2),
      ('Pruning',2),
      ('Mulching',2),
      ('Pest Management',2),
      ('Disease Management',2),
      ('Cover',2),
      ('Uncover',2),
      ('Build',2),
      ('Dismantle',2),
      ('Graze',3),
      ('Harvest',3),
      ('Recipes',3),
      ('Meals',3),
      ('Servings',3);

INSERT INTO public.plant_families(plant_family)
VALUES('Brassicaceae'),
      ('Lamiaceae'),
      ('Fabaceae'),
      ('Amaranthaceae'),
      ('Amaryllidaceae'),
      ('Apiaceae'),
      ('Solanaceae'),
      ('Cucurbitaceae'),
      ('Asteraceae');

INSERT INTO public.botanical_categories(botanical_category)
VALUES ('Herb'),
      ('Pod/Fruit'),
      ('Tuber, Herb'),
      ('Vegetable, Herb'),
      ('Bulb, Herb'),
      ('Tuber'),
      ('Vegetable, Herb, Seed'),
      ('Bulb');
