#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أمثلة على استخدام مستشارك القانوني - عون
Examples for using Legal Advisor - Awn

هذا الملف يحتوي على أمثلة برمجية لاستخدام نظام المستشار القانوني
"""

from legal_assistant import LegalAdvisor, LegalDatabase


def example_1_search_by_keyword():
    """مثال 1: البحث عن قانون بكلمة مفتاحية"""
    print("=" * 60)
    print("مثال 1: البحث عن قانون بكلمة مفتاحية")
    print("=" * 60)
    
    db = LegalDatabase()
    results = db.search_law("حقوق")
    
    print(f"\nوجدت {len(results)} نتيجة للبحث عن 'حقوق':\n")
    for result in results:
        print(f"• {result['العنوان']}")
        print(f"  النوع: {result['النوع']}")
        print(f"  الوصف: {result['الوصف']}\n")


def example_2_get_consultation():
    """مثال 2: الحصول على استشارة قانونية"""
    print("=" * 60)
    print("مثال 2: الحصول على استشارة قانونية")
    print("=" * 60)
    
    advisor = LegalAdvisor()
    
    # استفسار عن حقوق العمل
    print("\nالاستفسار: 'ما هي قوانين العمل؟'")
    print("-" * 60)
    consultation = advisor.provide_consultation("عمل")
    print(consultation)


def example_3_get_specific_law():
    """مثال 3: الحصول على قانون محدد"""
    print("\n" + "=" * 60)
    print("مثال 3: الحصول على قانون محدد")
    print("=" * 60)
    
    db = LegalDatabase()
    law = db.get_law_by_id("حقوق_الإنسان")
    
    if law:
        print(f"\nالعنوان: {law['العنوان']}")
        print(f"النوع: {law['النوع']}")
        print(f"الوصف: {law['الوصف']}")
        print("\nالمواد الرئيسية:")
        for i, article in enumerate(law['المواد'], 1):
            print(f"  {i}. {article}")


def example_4_list_all_categories():
    """مثال 4: عرض جميع الفئات القانونية"""
    print("\n" + "=" * 60)
    print("مثال 4: عرض جميع الفئات القانونية المتاحة")
    print("=" * 60)
    
    advisor = LegalAdvisor()
    categories = advisor.list_all_categories()
    
    print("\nالفئات المتاحة:")
    for category in categories:
        print(f"  {category}")


def example_5_multiple_searches():
    """مثال 5: البحث عن مواضيع متعددة"""
    print("\n" + "=" * 60)
    print("مثال 5: البحث عن مواضيع متعددة")
    print("=" * 60)
    
    advisor = LegalAdvisor()
    topics = ["إنسان", "مستهلك", "عمل"]
    
    for topic in topics:
        print(f"\n📌 الموضوع: '{topic}'")
        print("-" * 40)
        results = advisor.database.search_law(topic)
        if results:
            for result in results:
                print(f"  ✓ {result['العنوان']}")
        else:
            print("  ✗ لم يتم العثور على نتائج")


def run_all_examples():
    """تشغيل جميع الأمثلة"""
    print("\n")
    print("*" * 60)
    print("  أمثلة على استخدام مستشارك القانوني - عون  ")
    print("*" * 60)
    print("\n")
    
    example_1_search_by_keyword()
    example_2_get_consultation()
    example_3_get_specific_law()
    example_4_list_all_categories()
    example_5_multiple_searches()
    
    print("\n" + "=" * 60)
    print("انتهت الأمثلة")
    print("=" * 60)
    print("\nللمزيد من المعلومات، راجع ملف USAGE.md")
    print()


if __name__ == "__main__":
    run_all_examples()
