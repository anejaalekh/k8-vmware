from pprint import pprint
from unittest import TestCase

from k8_vmware.helpers.Test_VM import Test_VM


class test_Test_VMs(TestCase):

    def setUp(self):
        self.test_vm = Test_VM()

    def test__init__(self):
        assert self.test_vm.test_vm_name is "unit_tests_vm"

    def test_create__delete(self):
        vm = self.test_vm.create()
        assert self.test_vm.vm      == vm
        assert self.test_vm.vm_name == vm.name()

        delete_task = self.test_vm.delete()
        assert delete_task.info.state == "success"
