import os
import app
import unittest
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = 'mongodb://<dbuser>:<dbpassword>@ds123796.mlab.com:23796/jasons_cook_book'

class AppTestCase(unittest.TestCase):
        
        category = 'TestCat'
        categories = mongo.db.categories
        
        def TestCategory(self):
            categories = 'TestCat'
            self.assertEqual(AppTestCase.category, categories)
            
if __name__ == "__main__":
    unittest.main()