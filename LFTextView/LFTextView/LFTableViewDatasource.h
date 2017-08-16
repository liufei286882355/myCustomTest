//
//  LFTableViewDatasource.h
//  LFTextView
//
//  Created by 刘飞 on 2017/8/16.
//  Copyright © 2017年 刘飞. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>

//创建tableView的时候配置cell
//id cell可再调用的时候使用自定义的cell的类名称，
//id item可再调用的时候使用自定义的model的类的名称
typedef void(^TableViewCellConfigureBlock)(id cell, id item);


@interface LFTableViewDatasource : NSObject<UITableViewDataSource>

-(id)initWithItems:(NSArray *)itemsArray cellIdentifier:(NSString *)identifier configureCellBlock:(TableViewCellConfigureBlock)aConfigureCellBlock;

-(id)itemAtIndexPath:(NSIndexPath *)indexPath;


@end
