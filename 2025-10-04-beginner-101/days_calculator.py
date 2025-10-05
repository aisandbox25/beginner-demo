#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
日期计算器 - 计算距离未来日期的天数
"""

from datetime import datetime, date
import sys

def calculate_days_until_future_date(future_date_str):
    """
    计算距离未来日期的天数
    
    Args:
        future_date_str (str): 未来日期字符串，格式为 YYYY-MM-DD
    
    Returns:
        int: 距离今天的天数
    """
    try:
        # 解析用户输入的日期
        future_date = datetime.strptime(future_date_str, "%Y-%m-%d").date()
        
        # 获取今天的日期
        today = date.today()
        
        # 计算天数差
        days_difference = (future_date - today).days
        
        return days_difference, future_date, today
        
    except ValueError:
        raise ValueError("日期格式错误！请使用 YYYY-MM-DD 格式，例如：2025-12-25")

def main():
    """主函数"""
    print("=" * 50)
    print("📅 日期计算器 - 计算距离未来日期的天数")
    print("=" * 50)
    
    while True:
        try:
            # 获取用户输入
            future_date_str = input("\n请输入未来日期 (格式: YYYY-MM-DD，如 2025-12-25): ").strip()
            
            # 如果用户输入为空，退出程序
            if not future_date_str:
                print("👋 再见！")
                break
            
            # 计算天数
            days_difference, future_date, today = calculate_days_until_future_date(future_date_str)
            
            # 显示结果
            print(f"\n📊 计算结果:")
            print(f"今天日期: {today}")
            print(f"目标日期: {future_date}")
            
            if days_difference > 0:
                print(f"⏰ 距离目标日期还有: {days_difference} 天")
                
                # 额外信息
                if days_difference == 1:
                    print("🎉 明天就到了！")
                elif days_difference <= 7:
                    print("🔥 不到一周了！")
                elif days_difference <= 30:
                    print("📅 不到一个月了！")
                elif days_difference <= 365:
                    print("📆 不到一年了！")
                else:
                    years = days_difference // 365
                    remaining_days = days_difference % 365
                    print(f"🗓️  大约 {years} 年 {remaining_days} 天")
                    
            elif days_difference == 0:
                print("🎊 就是今天！")
            else:
                print(f"⏪ 目标日期已经过去了 {abs(days_difference)} 天")
                
        except ValueError as e:
            print(f"❌ 错误: {e}")
            print("💡 提示: 请确保日期格式正确，例如：2025-12-25")
            
        except KeyboardInterrupt:
            print("\n\n👋 程序被用户中断，再见！")
            break
        except Exception as e:
            print(f"❌ 发生未知错误: {e}")

if __name__ == "__main__":
    main()
