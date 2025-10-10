#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مستشارك القانوني - عون
Legal Assistant - Awn

نظام مساعد قانوني ذكي لتوفير المعلومات والاستشارات القانونية
"""

import sys
from typing import List, Dict, Optional


class LegalDatabase:
    """قاعدة بيانات القوانين"""
    
    def __init__(self):
        self.laws = self._initialize_laws()
    
    def _initialize_laws(self) -> Dict[str, Dict]:
        """تهيئة قاعدة بيانات القوانين الأساسية"""
        return {
            "حقوق_الإنسان": {
                "العنوان": "الإعلان العالمي لحقوق الإنسان",
                "النوع": "دولي",
                "الوصف": "وثيقة حقوق دولية تحدد الحقوق الأساسية للإنسان",
                "المواد": [
                    "المادة 1: يولد جميع الناس أحراراً متساوين في الكرامة والحقوق",
                    "المادة 2: لكل إنسان حق التمتع بكافة الحقوق والحريات دون تمييز",
                    "المادة 3: لكل فرد الحق في الحياة والحرية وسلامة شخصه"
                ]
            },
            "حقوق_العمل": {
                "العنوان": "قوانين العمل الأساسية",
                "النوع": "محلي ودولي",
                "الوصف": "قوانين تنظم العلاقة بين العامل وصاحب العمل",
                "المواد": [
                    "حق العامل في أجر عادل",
                    "حق العامل في ظروف عمل آمنة",
                    "حق العامل في الراحة والإجازات"
                ]
            },
            "حقوق_المستهلك": {
                "العنوان": "قانون حماية المستهلك",
                "النوع": "محلي",
                "الوصف": "قوانين تحمي حقوق المستهلكين",
                "المواد": [
                    "حق المستهلك في معرفة مواصفات المنتج",
                    "حق المستهلك في الاستبدال أو الاسترجاع",
                    "حق المستهلك في الشكوى والتعويض"
                ]
            }
        }
    
    def search_law(self, keyword: str) -> List[Dict]:
        """البحث عن قوانين بناءً على كلمة مفتاحية"""
        results = []
        keyword_lower = keyword.lower()
        
        for law_id, law_data in self.laws.items():
            if (keyword_lower in law_id.lower() or 
                keyword_lower in law_data['العنوان'].lower() or
                keyword_lower in law_data['الوصف'].lower()):
                results.append({
                    'المعرف': law_id,
                    **law_data
                })
        
        return results
    
    def get_law_by_id(self, law_id: str) -> Optional[Dict]:
        """الحصول على قانون محدد بواسطة المعرف"""
        return self.laws.get(law_id)


class LegalAdvisor:
    """المستشار القانوني"""
    
    def __init__(self):
        self.database = LegalDatabase()
    
    def provide_consultation(self, query: str) -> str:
        """تقديم استشارة قانونية بناءً على الاستفسار"""
        # البحث عن القوانين ذات الصلة
        relevant_laws = self.database.search_law(query)
        
        if not relevant_laws:
            return "عذراً، لم أتمكن من إيجاد قوانين ذات صلة بسؤالك. يرجى إعادة صياغة السؤال أو طلب المساعدة من مستشار قانوني متخصص."
        
        response = "بناءً على بحثي في قاعدة البيانات القانونية، إليك المعلومات ذات الصلة:\n\n"
        
        for i, law in enumerate(relevant_laws, 1):
            response += f"{i}. {law['العنوان']}\n"
            response += f"   النوع: {law['النوع']}\n"
            response += f"   الوصف: {law['الوصف']}\n"
            if law.get('المواد'):
                response += "   المواد الرئيسية:\n"
                for article in law['المواد'][:3]:  # عرض أول 3 مواد
                    response += f"   - {article}\n"
            response += "\n"
        
        response += "⚠️ تنبيه: هذه معلومات قانونية عامة. للحصول على استشارة قانونية مفصلة، يرجى التواصل مع محامٍ مختص."
        
        return response
    
    def list_all_categories(self) -> List[str]:
        """عرض جميع فئات القوانين المتاحة"""
        categories = []
        for law_id, law_data in self.database.laws.items():
            categories.append(f"• {law_data['العنوان']} ({law_id})")
        return categories


def main():
    """البرنامج الرئيسي"""
    print("=" * 60)
    print("        مرحباً بك في مستشارك القانوني - عون        ")
    print("        Your Legal Advisor - Awn        ")
    print("=" * 60)
    print()
    
    advisor = LegalAdvisor()
    
    # عرض القوائم المتاحة
    print("📚 الفئات القانونية المتاحة:")
    for category in advisor.list_all_categories():
        print(f"  {category}")
    print()
    
    # حلقة التفاعل الرئيسية
    while True:
        print("\nكيف يمكنني مساعدتك؟")
        print("1. طرح سؤال قانوني")
        print("2. البحث عن قانون معين")
        print("3. الخروج")
        
        choice = input("\nاختر رقم الخيار (1-3): ").strip()
        
        if choice == "1":
            query = input("\nما هو سؤالك القانوني؟ ")
            if query.strip():
                print("\n" + "=" * 60)
                print(advisor.provide_consultation(query))
                print("=" * 60)
        
        elif choice == "2":
            keyword = input("\nأدخل كلمة البحث: ")
            if keyword.strip():
                results = advisor.database.search_law(keyword)
                if results:
                    print(f"\nوجدت {len(results)} نتيجة/نتائج:\n")
                    for result in results:
                        print(f"• {result['العنوان']}")
                        print(f"  {result['الوصف']}\n")
                else:
                    print("\nلم يتم العثور على نتائج.")
        
        elif choice == "3":
            print("\nشكراً لاستخدامك مستشارك القانوني - عون")
            print("نتمنى أن نكون قد ساعدناك!")
            break
        
        else:
            print("\nخيار غير صحيح. يرجى اختيار رقم بين 1 و 3.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nتم إنهاء البرنامج. وداعاً!")
        sys.exit(0)
