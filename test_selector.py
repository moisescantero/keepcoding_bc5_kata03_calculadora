import unittest
import tkinterTestCase
import calculator

from tkinter import *
from tkinter import ttk

class TestSelector(tkinterTestCase.TkTestCase):
    def setUp(self):
        self.s = calculator.Selector(self.root)
        self.s.pack()
        self.s.wait_visibility()

    def tearDown(self):
        self.s.update()
        self.s.destroy()
    
    def test_render_OK(self):
        children = self.s.children
        self.assertEqual(self.s.status, "N")
        self.assertEqual(self.s.winfo_height(), 50)
        self.assertEqual(self.s.winfo_width(), 68)
        self.assertEqual(children["rbtn_romano"].config()["text"][4], "R")
        self.assertEqual(children["rbtn_normal"].config()["text"][4], "N")
        self.assertTrue(isinstance(children["rbtn_romano"], ttk.Radiobutton))#este y el de abajo son iguales
        self.assertIsInstance(children["rbtn_normal"], ttk.Radiobutton)#este y el de arriba son iguales
        self.assertTrue(children["rbtn_romano"].winfo_viewable(), 1)
        self.assertTrue(children["rbtn_normal"].winfo_viewable(), 1)
    
    def test_init_value_R(self):
        r_selector = calculator.Selector(self.root, "R")
        self.assertEqual(r_selector.status, "R")
        r_selector.update()
        r_selector.destroy()
    
    def test_click_change__status(self):
        rbtn_romano = self.s.children["rbtn_romano"]
        self.assertEqual(self.s.status, "N")
        self.assertEqual(self.s._Selector__value.get(), "N")#obtenemos valores de las variables de control usando get()
        rbtn_romano.invoke()
        self.assertEqual(self.s._Selector__value.get(), "R")#con nombre de la clase _Selector__value accedemos a los métodos privados
        self.assertEqual(self.s.status, "R")

if __name__=="__main__":
    unittest.main()