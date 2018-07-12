# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from model.models import UserInfo, ViewSpot, Route, RouteAppointment, ViewAppointment

# Create your tests here.

class ModelTest(TestCase):

    def setUp(self):
        UserInfo.objects.create_user(username='zjx123', password='q1w2e3', is_tourist=True)
        ViewSpot.objects.create(name='北海公园', address='北京市中心区', intro='是中国保留下来的最悠久最完整的皇家园林',
                                time='06:30~20:00', price='10.0')
        Route.objects.create(company_name='company1', route_num='c1', stand_num='2', stand_1_name='天安门广场',
                             date_1='2000-01-01', stand_2_name='北海公园', date_2='2000-01-02', price='50', end='2000-01-02')
        RouteAppointment.objects.create(company_name='company1', route_num='c1', tourist_name='zjx123')
        ViewAppointment.objects.create(view_name='北海公园', date='2000-01-01', person_num='5')

    def test_userinfo_models(self):
        result = UserInfo.objects.get(username='zjx123')
        self.assertTrue(result.check_password('q1w2e3'))
        self.assertTrue(result.is_tourist)

    def test_viewspot_models(self):
        result = ViewSpot.objects.get(name='北海公园')
        self.assertEqual(result.address, '北京市中心区')
        self.assertEqual(result.intro, '是中国保留下来的最悠久最完整的皇家园林')
        self.assertEqual(result.time, '06:30~20:00')
        self.assertEqual(result.price, 10.0)

    def test_route_models(self):
        result = Route.objects.get(company_name='company1')
        self.assertEqual(result.route_num, 'c1')
        self.assertEqual(result.stand_num, 2)
        self.assertEqual(result.stand_1_name, '天安门广场')
        self.assertEqual(result.stand_2_name, '北海公园')
        self.assertEqual(result.price, 50)

    def test_routeappointment_models(self):
        result = RouteAppointment.objects.get(company_name='company1')
        self.assertEqual(result.route_num, 'c1')
        self.assertEqual(result.tourist_name, 'zjx123')

    def test_viewappointment_models(self):
        result = ViewAppointment.objects.get(view_name='北海公园')
        self.assertEqual(result.person_num, 5)